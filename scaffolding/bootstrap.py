import os
from helpers.cli import pip, startproject
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import string_input
from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p

def bootstrap():
    cfg = get_cfg()
    project_name = string_input('Give the project a name')
    cfg['project_name'] = project_name
    set_cfg(cfg)
    os.mkdir('backend')
    os.chdir('backend')

    requirements_src = f(p('assets', 'reactjo-django') + '/requirements.txt', 'r')
    requirements_target = p('requirements')
    f(requirements_target, 'w', requirements_src)
    pip(['install', '-r', 'requirements.txt'])

    startproject(project_name)
