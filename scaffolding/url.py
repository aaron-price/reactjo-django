from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f

def scaffold_url():
    cfg = get_cfg
    Title = cfg['current_scaffold']['model']['Title']

    route = f('$assets/urls/new_api_url.py').format(
        Title=Title,
        Title_lower=Title.lower()
    )
    data = {
        'target': '# Register new routes below',
        'content': route
    }
    f('$api/url.py', 'a', data)
