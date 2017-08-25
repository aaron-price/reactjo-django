from helpers.cli import manage
from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p
from helpers.config_manager import get_cfg
import os

def setup_drf():
    cfg = get_cfg()
    project_name = cfg['project_name']

    os.chdir(p('backend_project'))
    manage(['startapp', 'api'])
    f(p('serializers.py'), 'w', '')
    f(p('permissions.py'), 'w', '')

    apps = "\n\t'rest_framework',\n\t'rest_framework.authtoken',\n\t'profiles_api'"
    data = {
        'target': ['INSTALLED_APPS'],
        'content': apps
    }
    path = p('settings')
