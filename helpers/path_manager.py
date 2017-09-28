from helpers.config_manager import get_cfg, set_cfg
from helpers.extension_constants import RC_HOME
import os

# /                                                         $su
# /prj_path                                                 $prj
# /prj_path/reactjorc/                                      $rc
# /prj_path/reactjorc/extensions/reactjo-django             $ext
# /prj_path/reactjorc/extensions/reactjo-django/assets      $assets
# /prj_path/output_name                                     $out
# /prj_path/output_name/output_name                         $main
# /prj_path/output_name/api                                 $api

# USAGE:
# from file_manager import file_manager as f
# f('$api/urls.py', '$')    # Returns the api/urls.py PATH as a string
# f('$api/urls.py', 'r')    # Returns the api/urls.py FILE as a string

def parse_shortcuts(path):
    cfg = get_cfg()
    output_name = cfg['backend_name']

    # Build all the paths
    su_path = cfg['paths']['super_root']
    prj_path = cfg['paths']['project_root']
    rc = os.path.join(su_path, 'reactjorc')
    ext = os.path.join(rc, 'extensions', RC_HOME)
    assets = os.path.join(ext, 'assets')
    out_path = os.path.join(prj_path, output_name)
    main_app = os.path.join(out_path, output_name)
    api = os.path.join(out_path, 'api')

    # Build the shortcuts
    shortcuts = {
        '$su': su_path,
        '$prj': prj_path,
        '$project': prj_path,
        '$rc': rc,
        '$ext': ext,
        '$extension': ext,
        '$assets': assets,
        '$out': out_path,
        '$output': out_path,
        '$main': main_app,
        '$api': api,
    }

    # Iterate over all shortcuts. If the path argument contains it, use it.
    parsed_string = path
    for key, value in shortcuts.items():
        parsed_string = os.path.join(parsed_string.replace(key, value))
    return parsed_string

def mkdir(path, name = None):
    path = parse_shortcuts(path)
    # Create directory
    if not os.path.exists(path):
        os.mkdir(path)

    # Create path entry in config
    cfg = get_cfg()
    if not name in cfg['paths'].keys() and name is not None:
        cfg['paths'][name] = path
        set_cfg(cfg)

def ls():
    print(" ")
    for name, path in get_cfg()['paths'].items():
        print(path, "\t|\tp(" + name + ")")
    print(" ")

def get_path(name):
    all_paths = get_cfg()['paths']
    path_names = all_paths.keys()
    ext_name = EXTENSION_NAME + "_" + name
    return ext_name if ext_name in all_paths else name
