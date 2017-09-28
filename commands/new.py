from scaffolding.main_structure import build_structure
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input

def new():
	backend_name = string_input('Name the Django backend app:', 'backend')
	need_users = boolean_input('Will you need user authentication?', 'y')
	cfg = get_cfg()
	cfg['need_users'] = str(need_users)
	cfg['backend_name'] = backend_name
	set_cfg(cfg)

	build_structure()
