from helpers.path_manager import mkdir
from helpers.file_manager import file_manager as f
from helpers.worklist import worklist as wl
import os, subprocess

def build_structure():
    prev_path = os.getcwd()
    mkdir(f('$out', 'path'))
    f('$out/requirements.txt', 'w', '$assets/requirements.txt')
    os.chdir(f('$out', 'path'))
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['django-admin', 'startproject', 'backend'])
    os.chdir(prev_path)
