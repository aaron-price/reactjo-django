from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f

def scaffold_permission():
    cfg = get_cfg()
    title = cfg['current_scaffold']['model']['Title']

    new_permission = f('$assets/permissions/new.py', 'r').format(Title = title)

    f('$api/permissions.py', 'a', new_permission)
