import os, subprocess

from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input
from scaffolding.models import scaffold_model
from scaffolding.view import scaffold_view
from scaffolding.serializer import scaffold_serializer
from scaffolding.permission import scaffold_permission
from scaffolding.url import scaffold_url

def scaffold():
	need_model = boolean_input('Do you need a new model?', 'y')
	cfg = get_cfg()

	if need_model:
		cfg['current_scaffold'] = {'model': {}}
		scaffold_model()
		prev_path = os.getcwd()
		os.chdir('$man')
		subprocess.run(['python', 'manage.py', 'makemigrations'])
		subprocess.run(['python', 'manage.py', 'migrate'])
		os.chdir(prev_path)
		set_cfg(cfg)

	scaffold_view()
	scaffold_serializer()
	scaffold_permission()
	scaffold_url()
