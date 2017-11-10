from helpers.file_manager import file_manager as f
from helpers.config_manager import get_cfg
from helpers.worklist import worklist as wl

"""Builds the django admin.py file"""
def scaffold_admin():
    cfg = get_cfg()
    title = cfg['current_scaffold']['model']['title']
    new_admin = f('$assets/admin/new.py', 'r').format(title=title)
    f('$api/admin.py', 'a', new_admin)
    wl('Added admin entry')
