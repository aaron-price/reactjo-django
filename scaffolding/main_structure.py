from helpers.path_manager import mkdir
from helpers.file_manager import file_manager as f
from helpers.worklist import worklist as wl
import os, subprocess
from helpers.extension_constants import OUTPUT_HOME
from textwrap import dedent

def build_settings_structure():
    path_above_settings = f(
        '$out/{}/{}'.format(OUTPUT_HOME, OUTPUT_HOME),
        '$')
    settings_dir = os.path.join(path_above_settings, 'settings')

    # settings dir
    mkdir(settings_dir, 'settings_dir')

    # __init__ file
    init_asset = f('$assets/settings_init.py', 'r')
    init_output = f(os.path.join(settings_dir, '__init__.py'), '$')
    f(init_output, 'w', init_asset)

    # Settings variables
    old_settings_path = f(os.path.join(path_above_settings, 'settings.py'), '$')
    base_settings_path = f(os.path.join(settings_dir, 'base.py'), '$')
    prod_settings_path = f(os.path.join(settings_dir, 'production.py'), '$')
    dev_settings_path = f(os.path.join(settings_dir, 'development.py'), '$')

    # Append apps and AUTH_USER_MODEL
    data = {
        'target': ['INSTALLED_APPS'],
        'content': "\n\t'api',\n\t'rest_framework',\n\t'rest_framework.authtoken',\n\t'corsheaders',"
    }
    f(old_settings_path, 'a', data)
    f(old_settings_path, 'a', "\nAUTH_USER_MODEL = 'api.UserProfile'")

    # Copy settings files into dir, and remove original
    old_settings_file = f(old_settings_path, 'r')
    f(base_settings_path, 'w', old_settings_file)
    f(prod_settings_path, 'w', old_settings_file)
    f(dev_settings_path, 'w', old_settings_file)
    f(os.path.join(settings_dir, '__init__.py'), 'w', ' ')
    f(old_settings_path, 'd')

    # ENV specific configs
    data = {
        'target': "ALLOWED_HOSTS =",
        'content': "ALLOWED_HOSTS = ['localhost', '127.0.0.1']"
    }
    f(dev_settings_path, 'w', data)

    data = {
        'target': 'DEBUG = True',
        'content': 'DEBUG = False'
    }
    f(prod_settings_path, 'w', data)

    cors = dedent("""
    CORS_ORIGIN_WHITELIST = (
    	'localhost:3000'
    	'127.0.0.1:3000'
    )
    """)
    f(dev_settings_path, 'a', cors)

def build_structure():
    # Pip install require
    prev_path = os.getcwd()
    mkdir(f('$out', 'path'))
    f('$out/requirements.txt', 'w', '$assets/requirements.txt')
    os.chdir(f('$out', 'path'))
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

    # Start django project
    subprocess.run(['django-admin', 'startproject', 'backend'])
    os.chdir(prev_path)

    build_settings_structure()
