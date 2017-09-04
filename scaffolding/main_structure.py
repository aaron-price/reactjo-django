from helpers.path_manager import mkdir
from helpers.file_manager import file_manager as f
from helpers.worklist import worklist as wl
import os, subprocess
from helpers.extension_constants import OUTPUT_HOME
from textwrap import dedent
from scaffolding.settings import build_settings
from helpers.config_manager import get_cfg

def user_auth_structure():
    cfg = get_cfg()
    if cfg['need_users'] == 'True':
        f('$man/api/models.py', 'a', '$assets/models/UserProfile.py')
        f('$man/api/serializers.py', 'a', '$assets/serializers/user_profile.py')
        f('$man/api/views.py', 'a', '$assets/views/users.py')
        f('$man/api/permissions.py', 'a', '$assets/permissions/post_own_content.py')
        f('$man/api/permissions.py', 'a', '$assets/permissions/update_own_profile.py')

        # Puts the user routes below the router, but above urlpatterns
        route_flag = '# Register new routes below'
        route_start = f(
            '$man/api/urls.py',
            'r').find(route_flag) + len(route_flag) + 1
        old_urls = f('$man/api/urls.py', 'r')
        begin = old_urls[:route_start]
        mid = f('$assets/urls/user_urls.py', 'r')
        end = old_urls[route_start:]
        f('$man/api/urls.py', 'w', begin + mid + end)
        wl('Added a model, serializer, urls, and view for Users')

def build_structure():
    # Pip install require
    prev_path = os.getcwd()

    mkdir(f('$out', '$'))
    f('$out/requirements.txt', 'w', '$assets/requirements.txt')
    os.chdir(f('$out', '$'))
    subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])
    wl('Installed pip packages', prev_path)

    # Start django project
    subprocess.run(['django-admin', 'startproject', 'backend'])
    wl('Created Django project', prev_path)
    os.chdir('backend')
    subprocess.run(['python3', 'manage.py', 'startapp', 'api'])
    wl('Create api app', prev_path)

    build_settings(prev_path)
    os.chdir(prev_path)
    f('$man/backend/urls.py', 'w', '$assets/urls/root_urls.py')
    wl('Add /api and /api-auth to root urls')

    f('$man/api/models.py', 'w', '$assets/models/imports.py')
    f('$man/api/serializers.py', 'w', '$assets/serializers/imports.py')
    f('$man/api/permissions.py', 'w', '$assets/permissions/imports.py')
    f('$man/api/views.py', 'w', '$assets/views/imports.py')
    f('$man/api/urls.py', 'w', '$assets/urls/base_app_url.py')
    wl('Prepped the api views, models, urls, and serializers files')
    user_auth_structure()

    os.chdir(f('$man', '$'))
    subprocess.run(['python3', 'manage.py', 'makemigrations'])
    subprocess.run(['python3', 'manage.py', 'migrate'])
    os.chdir(prev_path)
    wl('Ran some database migrations')
