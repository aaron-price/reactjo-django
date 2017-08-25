from helpers.cli import manage
from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p

def setup_drf():
    manage(['startapp', 'api'])
    f(p('serializers.py'), 'w', '')
    f(p('permissions.py'), 'w', '')

    apps = "\n\t'rest_framework',\n\t'rest_framework.authtoken',\n\t'profiles_api'"
    data = {
        'target': ['INSTALLED_APPS'],
        'content': apps
    }
    path = p('settings')
