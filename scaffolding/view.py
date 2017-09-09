from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f

def scaffold_view():
    cfg = get_cfg()
    new_view = f('$assets/views/new.py', 'r').format(
        Title = cfg['current_scaffold']['model']['title'],
    )
    f('$api/views.py', 'a', new_view)
