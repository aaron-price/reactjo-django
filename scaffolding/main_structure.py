from helpers.path_manager import mkdir
from helpers.file_manager import file_manager as f
from helpers.worklist import worklist as wl
import os, subprocess
from helpers.extension_constants import OUTPUT_HOME
from textwrap import dedent
from scaffolding.settings import build_settings

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

    f('$man/api/models.py', 'w', '$assets/models/base_models.py')
    wl('Built a default User model')

    os.chdir(f('$man', '$'))
    subprocess.run(['python3', 'manage.py', 'makemigrations'])
    subprocess.run(['python3', 'manage.py', 'migrate'])
    os.chdir(prev_path)
