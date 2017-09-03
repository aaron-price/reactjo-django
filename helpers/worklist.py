from helpers.config_manager import get_cfg, set_cfg

def worklist(string):
	cfg = get_cfg()
	if not 'worklist' in cfg:
		cfg['worklist'] = []

	cfg['worklist'].append(string)
	set_cfg(cfg)
