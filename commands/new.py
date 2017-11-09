from scaffolding.main_structure import build_structure
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input, string_input

def new():
	backend_name = string_input('Name the Django backend app:', 'backend')
	need_users = True # Kept for legacy
	cfg = get_cfg()
	cfg['need_users'] = str(need_users)
	cfg['backend_name'] = backend_name
	set_cfg(cfg)

	try:
		build_structure()
	except Exception as e:
		print(e)
