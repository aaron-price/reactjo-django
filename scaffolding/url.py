from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input

def scaffold_url():
    cfg = get_cfg()
    title = cfg['current_scaffold']['model']['title']

    route = f('$assets/urls/new_api_url.py', 'r').format(
        title=title,
        title_lower=title.lower()
    )
    data = {
        'target': '# Register new routes below',
        'content': '# Register new routes below\n' + route
    }
    f('$api/urls.py', 'w', data)
    wl('Created url route')
