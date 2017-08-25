import os
import subprocess

def bootstrap():
    # Project name and config
    from helpers.config_manager import get_cfg, set_cfg
    from helpers.ui import string_input, boolean_input
    cfg = get_cfg()
    project_name = string_input('Give the project a name')
    cfg['project_name'] = project_name
    set_cfg(cfg)

    # Pip requirements
    from helpers.cli import pip, startproject, startapp
    from helpers.file_manager import file_manager as f
    from helpers.path_manager import path_manager as p
    f(p('backend'), 'mkdir')
    os.chdir(p('backend'))
    requirements_src = f(p('assets', ext_name = 'reactjo_django') + '/requirements.txt','r')
    requirements_target = p('requirements')
    f(requirements_target, 'w', requirements_src)
    pip(['install', '-r', p('requirements')])

    # Build Django project
    os.chdir(p('backend'))
    startproject(project_name)

    # Settings
    f(p('settings'), 'mkdir')

    settings_init = f(p('assets', ext_name = 'reactjo_django') + '/settings_init.py', 'r')
    f(p('settings') + '/__init__.py', 'w', settings_init)

    settings_file = f(p('app', app_name = project_name) + '/settings.py' , 'r')
    f(p('settings') + '/base.py', 'w', settings_file)
    f(p('settings') + '/development.py', 'w', settings_file)
    f(p('settings') + '/production.py', 'w', settings_file)
    f(p('app', app_name = project_name) + '/settings.py', 'd')

    # API app
    startapp('api')

    from helpers.cli import manage
    manage(['migrate'])
