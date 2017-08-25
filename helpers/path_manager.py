from helpers.config_manager import get_cfg
import os

cfg = get_cfg()
PROJECT_NAME = cfg['project_name']
EXTENSION_NAME = 'django'

# Organization:
# Here's the default structure and how to return a string path for ANYTHING.


# TOP LEVEL PATHS
# None of these should be version controlled
#
# / 								p('super_root')
# 	 /venv							p('super_root') + '/venv'
# 	 /reactjorc 					p('reactjorc')
#	 /backend						p('backend')
#	 /frontend						p('frontend')


# REACTJORC PATHS
# Don't put these in production, or version control
#
# /reactjorc 						p('reactjorc')
# 	/config.json 					p('config')
# 	/extensions 					p('extensions')
# 		/django						p('extensions', 'django')
# 			/assets/ 				p('assets', 'django')
# 			/helpers/ 				p('helpers', 'django')
# 			/entry.py 				p('extensions', 'django') + '/entry.py'

# BACKEND PATHS
# The Django codebase which runs the API.
# This assumes the project is named "www", and has an extra app named "foo"
#
# /backend 							p('backend')
# 	/requirements.txt				p('requirements.txt')
# 	/www							p('backend_project')
# 		/manage.py					p('manage.py')
# 		/www						p('app', 'www')
#			/settings				p('settings')
# 				base.py				p('base_settings')
# 				production.py		p('prod_settings')
# 				development.py		p('dev_settings')
# 			/views.py 				p('views', 'www')
# 			/urls.py 				p('urls', 'www')
# 			/tests.py 				p('tests', 'www')
#			/serializers.py			p('serializers', 'www')
#			/permissions.py			p('permissions', 'www')
#			/models.py				p('models', 'www')
# 		/api 						p('app', 'api')
# 			/views.py 				p('views','api')
# 			/urls.py 				p('urls','api')
# 			/tests.py 				p('tests','api')
#			/serializers.py			p('serializers')
#			/permissions.py			p('permissions')
#			/models.py				p('models', 'api')
# 		/foo 						p('app', 'foo')
# 			/views.py 				p('views','foo')
# 			/urls.py 				p('urls','foo')
# 			/tests.py 				p('tests','foo')
#			/serializers.py			p('serializers', 'www')
#			/permissions.py			p('permissions', 'www')
#			/models.py				p('models', 'foo')

# FRONTEND PATHS
# The Node + express server that runs react and all things client side. Based on create-react-app
#
# /frontend 						p('frontend')
#	/config 						p('fe_config')
#	/node_modules 					p('node_modules')
#	/package.json 					p('package_json')
#	/public 						p('public')
# 	/src 							p('src')
#	/.babelrc 						p('babelrc')


# SUPER ROOT
def super_root():
	return os.path.join(get_cfg()['paths']['super_root'])

# REACTJORC
def reactjorc():
	return os.path.join(super_root(), 'reactjorc')

def config():
	return os.path.join(reactjorc(), 'config.json')

def extensions():
	return os.path.join(reactjorc(), 'extensions')

def assets(ext_name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), ext_name), 'assets')

def helpers(ext_name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), ext_name), 'helpers')

def helpers(ext_name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), ext_name), 'helpers')

def scaffolding(ext_name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), ext_name), 'scaffolding')

# BACKEND
def backend():
	return os.path.join(super_root(), 'backend')

def requirements():
	return os.path.join(backend(), 'requirements.txt')

def backend_project():
	return os.path.join(backend(), PROJECT_NAME)

def manage_py():
	return os.path.join(backend_project(), 'manage.py')

def app(app_name):
	return os.path.join(backend_project(), app_name)

def settings():
	return os.path.join(app(app_name = PROJECT_NAME), 'settings')

def views(app_name):
	return os.path.join(app(app_name), 'views.py')

def models(app_name):
	return os.path.join(app(app_name), 'models.py')

def admin(app_name):
	return os.path.join(app(app_name), 'admin.py')

def urls(app_name):
	return os.path.join(app(app_name), 'urls.py')

def tests(app_name):
	return os.path.join(app(app_name), 'tests.py')

def serializers(app_name = 'api'):
	return os.path.join(app(app_name = 'api'), 'serializers.py')

def permissions(app_name = 'api'):
	return os.path.join(app(app_name = 'api'), 'permissions.py')

# FRONTEND
def frontend():
	return os.path.join(super_root(), 'frontend')

def webpack():
	return os.path.join(frontend(), 'webpack.config.js')

def path_manager(query, **kwargs):
	string = ''
	query = query.lower().replace(' ', '').replace('-', '').replace('_', '').replace('.', '')

	# SUPER ROOT
	if query in ['superroot', 'super']:
		string = super_root()

	# REACTJORC
	if query in ['reactjorc']:
		string = reactjorc()
	if query in ['config','cfg','configjson']:
		string = config()
	if query in ['extensions']:
		string = extensions()
	if query in ['assets']:
		string = assets(**kwargs)
	if query in ['helpers', 'helper']:
		string = helpers(**kwargs)
	if query in ['scaffold', 'scaffolding']:
		string = scaffolding(**kwargs)

	# BACKEND
	if query in ['backend']:
		string = backend(**kwargs)
	if query in ['requirements', 'requirementstxt']:
		string = requirements(**kwargs)
	if query in ['backendproject']:
		string = backend_project()
	if query in ['manage', 'managepy']:
		string = manage_py()
	if query in ['settings', 'settingsroot']:
		string = settings()
	if query in ['settingsbase', 'basesettings']:
		string = os.path.join(settings(), 'base.py')
	if query in ['settingsdev','settingsdevelopment', 'devsettings','developmentsettings']:
		string = os.path.join(settings(), 'development.py')
	if query in ['settingsprod','settingsproduction', 'prodsettings', 'productionsettings']:
		string = os.path.join(settings(), 'production.py')
	if query in ['app']:
		string = app(**kwargs)
	if query in ['views','viewspy']:
		string = views(**kwargs)
	if query in ['models','modelspy']:
		string = models(**kwargs)
	if query in ['urls','urlspy']:
		string = urls(**kwargs)
	if query in ['admin','adminpy']:
		string = admin(**kwargs)
	if query in ['tests','testspy']:
		string = tests(**kwargs)
	if query in ['serializers','serializerspy']:
		string = serializers(**kwargs)
	if query in ['permissions','permissionspy']:
		string = permissions(**kwargs)

	if query in ['frontend']:
		string = frontend()
	if query in ['webpack', 'webpackconfig', 'webpackconfigjs']:
		string = webpack()


	return string
