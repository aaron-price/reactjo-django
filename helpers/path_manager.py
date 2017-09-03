from helpers.config_manager import get_cfg, set_cfg
from helpers.extension_constants import OUTPUT_HOME, RC_HOME
import os

def parse_shortcuts(path):
    cfg = get_cfg()
    su_path = cfg['paths']['super_root']
    prj_path = cfg['paths']['project_root']
    out_path = os.path.join(prj_path, OUTPUT_HOME)

    shortcuts = {
        '$su': su_path,
        '$rc': os.path.join(su_path, 'reactjorc'),
        '$project': prj_path,
        '$prj': prj_path,
        '$output': os.path.join(prj_path, OUTPUT_HOME),
        '$out': os.path.join(prj_path, OUTPUT_HOME),
        '$extension': os.path.join(su_path, 'reactjorc/extensions', RC_HOME),
        '$ext': os.path.join(su_path, 'reactjorc/extensions', RC_HOME),
        '$assets': os.path.join(su_path, 'reactjorc/extensions', RC_HOME, 'assets'),
    }
    if 'shortcuts' not in cfg['paths'].keys():
        cfg['paths']['shortcuts'] = shortcuts
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
