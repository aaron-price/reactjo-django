from scaffolding.main_structure import build_structure
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input

def new():
	need_users = boolean_input('Will you need user authentication?', 'y')
	cfg = get_cfg()
	cfg['need_users'] = str(need_users)
	set_cfg(cfg)

	build_structure()
