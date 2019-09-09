from .base_settings import *

if DEBUG:
    from .dev_setttings import *
else:
    from .server_settings import *
