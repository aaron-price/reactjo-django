from helpers.path_manager import mkdir
from helpers.file_manager import file_manager as f
from helpers.worklist import worklist as wl
import os, subprocess
from textwrap import dedent
from scaffolding.settings import build_settings
from scaffolding.users import scaffold_users
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input

def pip_install():
    # Solves chicken and egg problem.
    # Temporarily create requirements, installs it, removes it,
    # We make it again somewhere else after directories exist.
    f('$su/requirements.txt', 'w', '$assets/requirements.txt')
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    f('$su/requirements.txt', 'd')
    wl('Installed pip packages')

def build_structure():
    cfg = get_cfg()
    prev_path = os.getcwd()
    pip_install()

    # Start django project
    os.chdir(f('$prj', '$'))
    backend_name = cfg['backend_name']
    subprocess.run(['django-admin', 'startproject', backend_name])
    wl('Created Django project', prev_path)

    # Make api app.
    os.chdir(f('$out', '$'))
    subprocess.run(['python', 'manage.py', 'startapp', 'api'])
    wl('Created api app', prev_path)

    need_prod = boolean_input('Will you be deploying this to heroku?', 'y')
    cfg = get_cfg()
    cfg['need_production'] = need_prod
    set_cfg(cfg)

    build_settings(prev_path)

    f('$main/urls.py', 'w', '$assets/urls/root_urls.py')
    wl('Add /api and /api-auth to root urls')

    # Api files
    f('$api/models.py', 'w', '$assets/models/imports.py')
    f('$api/serializers.py', 'w', '$assets/serializers/imports.py')
    f('$api/permissions.py', 'w', '$assets/permissions/base.py')
    f('$api/views.py', 'w', '$assets/views/imports.py')
    f('$api/urls.py', 'w', '$assets/urls/app_urls_without_users.py')
    f('$api/admin.py', 'w', '$assets/admin/imports.py')
    wl('Prepped the api files')

    # Prepare for heroku
    mkdir('$out/utils')
    f('$out/utils/renderers.py', 'w', '$assets/utils/renderers.py')
    f('$out/requirements.txt', 'w', '$assets/requirements.txt')
    if need_prod:
        procfile = f('$assets/Procfile.txt', 'r').replace(
            'backend', backend_name)
        f('$out/Procfile', 'w', procfile)
        f('$out/runtime.txt', 'w', '$assets/runtime.txt')
        f('$out/.env', 'w', '$assets/env.txt')

        # Install some production specific packages
        f('$out/requirements.txt', 'w', '$assets/requirements_prod.txt')
        prev_path = os.getcwd()
        os.chdir(f('$out', '$'))
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        os.chdir(prev_path)

    # Users
    cfg = get_cfg()
    if cfg['need_users'] == 'True':
        scaffold_users()

    # Migrations
    if boolean_input('Run DB migrations now?', 'y'):
        os.chdir(f('$out', '$'))
        subprocess.run(['python', 'manage.py', 'makemigrations'])
        subprocess.run(['python', 'manage.py', 'migrate'])
        os.chdir(prev_path)
        wl('Ran some database migrations')

        # Superusers
        need_su = boolean_input('Would you like to create a superuser now?', 'y')
        if need_su:
            os.chdir(f('$out', '$'))
            subprocess.run(['python', 'manage.py', 'createsuperuser'])
            os.chdir(prev_path)
