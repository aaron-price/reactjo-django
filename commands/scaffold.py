from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input
from scaffolding.models import scaffold_model

def scaffold():
	need_model = boolean_input('Do you need a new model?', 'y')
	cfg = get_cfg()
	cfg['current_scaffold'] = {'model': {}}
	set_cfg(cfg)

	scaffold_model()
