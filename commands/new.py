from scaffolding.bootstrap import bootstrap
from scaffolding.setup_drf import setup_drf
from scaffolding.update_settings import update_settings

def new():
	bootstrap()
	update_settings()
	setup_drf()
