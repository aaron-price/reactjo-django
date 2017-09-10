from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input

def scaffold_permission():
    if boolean_input('Add a permission?', 'y'):
        cfg = get_cfg()
        title = cfg['current_scaffold']['model']['title']

        new_permission = f('$assets/permissions/new.py', 'r').format(
            title = title,
            action = 'Create'
        )

        f('$api/permissions.py', 'a', new_permission)
