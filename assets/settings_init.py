import os
from .base import *

if os.environ.get('IS_PRODUCTION'):
    from .production import *
else:
    from .development import *
