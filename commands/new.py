from scaffolding.bootstrap import bootstrap
from scaffolding.update_settings import update_settings
from scaffolding.user_auth import user_auth
from helpers.cli import manage
from helpers.ui import boolean_input

def new():
	bootstrap()
	update_settings()
	user_auth()
	manage(['makemigrations'])
	manage(['migrate'])

	need_su = boolean_input('Would you like to create a superuser now?' ,'y')
	if need_su:
	    manage(['createsuperuser'])
