import os, subprocess

from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input
from scaffolding.models import scaffold_model
from scaffolding.view import scaffold_view
from scaffolding.serializer import scaffold_serializer
from scaffolding.permission import scaffold_permission
from scaffolding.admin import scaffold_admin
from helpers.file_manager import file_manager as f

def scaffold():
	need_model = boolean_input('Do you need a new model?', 'y')
	cfg = get_cfg()

	if need_model:
		cfg['current_scaffold'] = {'model': {}}
		set_cfg(cfg)

		scaffold_model()
		prev_path = os.getcwd()
		os.chdir(f('$man', '$'))
		subprocess.run(['python', 'manage.py', 'makemigrations'])
		subprocess.run(['python', 'manage.py', 'migrate'])
		os.chdir(prev_path)

		# scaffold_permission()
		scaffold_view()
		scaffold_serializer()
		scaffold_admin()
