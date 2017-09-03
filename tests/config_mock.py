# from helpers.file_manager import file_manager as f
from helpers.config_manager import get_cfg, set_cfg
import os
import shutil
config_asset_path = os.path.join(os.getcwd(), 'tests/assets/config.js')
reactjorc_path = os.path.join(os.getcwd(), 'reactjorc')
config_destination_path = os.path.join(os.getcwd(), 'reactjorc/config.json')

# file read/write functions duplicated to get around circular import issue
def file_read(path):
    return open(path, 'r').read()

def file_write(path, content):
    file = open(path, 'w')
    file.write(content)
    file.close()

def setup_config():
	src = file_read(config_asset_path)
	target = config_destination_path
	if not os.path.isdir(reactjorc_path):
		os.mkdir(reactjorc_path)
	file_write(target, src)
	cfg = get_cfg()
	super_root = os.getcwd()
	project_name = 'www'

	cfg['paths']['super_root'] = super_root
	cfg['paths']['project_root'] = os.path.join(super_root, project_name)

	set_cfg(cfg)

def teardown_config():
	shutil.rmtree(reactjorc_path)
