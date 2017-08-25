from scaffolding.bootstrap import bootstrap
from scaffolding.update_settings import update_settings
from scaffolding.user_auth import user_auth

def new():
	bootstrap()
	update_settings()
	user_auth()
