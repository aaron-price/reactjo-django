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
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    wl('Installed pip packages', prev_path)

    # Start django project
    subprocess.run(['django-admin', 'startproject', 'backend'])
    wl('Created Django project', prev_path)
    os.chdir(f('$out/backend', '$'))
    subprocess.run(['python', 'manage.py', 'startapp', 'api'])
    wl('Create api app', prev_path)

    build_settings()
