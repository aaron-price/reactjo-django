from helpers.path_manager import mkdir
from helpers.file_manager import file_manager as f
from helpers.worklist import worklist as wl
import os, subprocess
from helpers.extension_constants import OUTPUT_HOME
from textwrap import dedent
from scaffolding.settings import build_settings
from scaffolding.users import scaffold_users
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input

def build_structure():
    # Pip install require
    prev_path = os.getcwd()

    mkdir(f('$out', '$'))
    f('$out/requirements.txt', 'w', '$assets/requirements.txt')
    os.chdir(f('$out', '$'))
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    wl('Installed pip packages', prev_path)

    # Start django project
    subprocess.run(['django-admin', 'startproject', 'backend'])
    wl('Created Django project', prev_path)
    os.chdir('backend')
    subprocess.run(['python', 'manage.py', 'startapp', 'api'])
    wl('Create api app', prev_path)

    build_settings(prev_path)
    os.chdir(prev_path)
    f('$man/backend/urls.py', 'w', '$assets/urls/root_urls.py')
    wl('Add /api and /api-auth to root urls')

    # Api files
    f('$man/api/models.py', 'w', '$assets/models/imports.py')
    f('$man/api/serializers.py', 'w', '$assets/serializers/imports.py')
    f('$man/api/permissions.py', 'w', '$assets/permissions/base.py')
    f('$man/api/views.py', 'w', '$assets/views/imports.py')
    f('$man/api/urls.py', 'w', '$assets/urls/app_urls_without_users.py')
    f('$man/api/admin.py', 'w', '$assets/admin/imports.py')
    wl('Prepped the api files')

    # Users
    cfg = get_cfg()
    if cfg['need_users'] == 'True':
        scaffold_users()

    # Migrations
    if boolean_input('Run DB migrations now?', 'y'):
        os.chdir(f('$man', '$'))
        subprocess.run(['python', 'manage.py', 'makemigrations'])
        subprocess.run(['python', 'manage.py', 'migrate'])
        os.chdir(prev_path)
        wl('Ran some database migrations')

        # Superusers
        need_su = boolean_input('Would you like to create a superuser now?', 'y')
        if need_su:
            os.chdir(f('$man', '$'))
            subprocess.run(['python', 'manage.py', 'createsuperuser'])
            os.chdir(prev_path)
