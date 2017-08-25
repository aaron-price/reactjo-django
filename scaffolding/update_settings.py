from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p

def update_settings():
    all_settings = [p('base_settings') ,p('dev_settings'), p('prod_settings')]
    for s in all_settings:
        apps = "\n\t'rest_framework',\n\t'rest_framework.authtoken',\n\t'profiles_api'"
        data = {
            'target': ['INSTALLED_APPS'],
            'content': apps
        }
        f(s, 'a', data)

        base = 'os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))'
        data = {
            'target': 'BASE_DIR = ',
            'content': 'BASE_DIR = ' + base
        }
        f(s, 'w', data)

    # DEV ONLY
    data = {
        'target': "ALLOWED_HOSTS = []",
        'content': "ALLOWED_HOSTS = ['localhost']"
    }
    f(p('dev_settings'), 'a', data)

    # PROD ONLY
    data = {
        'target': 'DEBUG = True',
        'content': 'DEBUG = False'
    }
    f(p('prod_settings'), 'w', data)
