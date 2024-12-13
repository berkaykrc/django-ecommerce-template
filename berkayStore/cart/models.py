from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from product.models import Product

SHOPPINGCART_STATUS = [
    ('deleted', 'Silindi'),
    ('waiting', 'Bekliyor'),
    ('purchased', 'Satin Alindi')
]


class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.product.title} {self.price} TL'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.CASCADE,
        null=True
    )
    session_key = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    items = models.ManyToManyField(ShoppingCartItem, blank=True)
    total_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )
    status = models.CharField(
        choices=SHOPPINGCART_STATUS,
        default='waiting',
        max_length=15
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.pk} - {self.total_price} - Status {self.status}'

    def total_price_update(self):
        if self.status == "waiting":
            total_price = 0
            for item in self.items.all():
                if item.is_deleted == False:
                    total_price += item.price
            self.total_price = total_price
            self.save()


@receiver(post_save, sender=ShoppingCartItem)
def shopping_cart_item_receiver(sender, instance, created, *args, **kwargs):
    if created:
        instance.price = instance.product.price
        instance.save()
    instance.shopping_cart_add.last().total_price_update()


@receiver(m2m_changed, sender=ShoppingCart.items.through)
def shopping_cart_receive(sender, instance, *args, **kwargs):
    instance.total_price_update()
