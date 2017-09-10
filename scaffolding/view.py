from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input

def scaffold_view():
    if boolean_input('Need a view?'):
        cfg = get_cfg()
        new_view = f('$assets/views/new.py', 'r').format(
            title = cfg['current_scaffold']['model']['title'],
        )
        f('$api/views.py', 'a', new_view)
