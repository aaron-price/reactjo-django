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

    # Edit old settings file
    data = {
        'target': ['INSTALLED_APPS'],
        'content': "\n\t'api',\n\t'rest_framework',\n\t'rest_framework.authtoken',\n\t'corsheaders',"
    }
    f(old_settings_path, 'a', data)
    f(old_settings_path, 'a', "\nAUTH_USER_MODEL = 'api.UserProfile'")

    drf_settings = dedent("""
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        )
    }
    """)
    f(old_settings_path, 'a', drf_settings)

    data = {
        'target': "BASE_DIR =",
        'content': "BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))"
    }
    f(old_settings_path, 'w', data)


    # Add cors to middle of Middleware by replacing the whole list.
    old_file = f(old_settings_path, 'r')
    mid_i_begin = old_file.find('MIDDLEWARE = [')
    mid_i_end = old_file.find(']', mid_i_begin) + 1

    new_middle = dedent("""\
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]""")

    # Assemble the pieces.
    begin = old_file[:mid_i_begin]
    end = old_file[mid_i_end:]
    f(old_settings_path, 'w', begin + new_middle + end)

    # Copy settings files into dir, and remove original
    old_settings_file = f(old_settings_path, 'r')
    f(base_settings_path, 'w', old_settings_file)
    f(prod_settings_path, 'w', old_settings_file)
    f(dev_settings_path, 'w', old_settings_file)
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

    cors = dedent("""\
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
