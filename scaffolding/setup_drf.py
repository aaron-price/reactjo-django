from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p
from helpers.config_manager import get_cfg
import os

def setup_drf():
    f(p('serializers.py'), 'w', '')
    f(p('permissions.py'), 'w', '')
