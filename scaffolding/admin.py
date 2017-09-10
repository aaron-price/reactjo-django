from helpers.file_manager import file_manager as f
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input

def scaffold_admin():
    if boolean_input('Add an admin field?', 'y'):
        cfg = get_cfg()
        title = cfg['current_scaffold']['model']['title']
        new_admin = f('$assets/admin/new.py', 'r').format(title=title)
        f('$api/admin.py', 'a', new_admin)
