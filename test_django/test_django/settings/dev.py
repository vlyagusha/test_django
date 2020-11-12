from test_django.settings.base import *

try:
    from test_django.settings.local import *
except ImportError:
    pass
