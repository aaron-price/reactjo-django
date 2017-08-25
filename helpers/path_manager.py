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

def assets(name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), name), 'assets')

def helpers(name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), name), 'helpers')

def helpers(name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), name), 'helpers')

def scaffolding(name = EXTENSION_NAME):
	return os.path.join(os.path.join(extensions(), name), 'scaffolding')

# BACKEND
def backend():
	return os.path.join(super_root(), 'backend')

def requirements():
	return os.path.join(backend(), 'requirements.txt')

def backend_project():
	return os.path.join(backend(), PROJECT_NAME)

def manage_py():
	return os.path.join(backend_project(), 'manage.py')

def app(name):
	return os.path.join(backend_project(), name)

def settings():
	return os.path.join(app(name = PROJECT_NAME), 'settings')

def views(name):
	return os.path.join(app(name), 'views.py')

def models(name):
	return os.path.join(app(name), 'models.py')

def admin(name):
	return os.path.join(app(name), 'admin.py')

def urls(name):
	return os.path.join(app(name), 'urls.py')

def tests(name):
	return os.path.join(app(name), 'tests.py')

def serializers(name = 'api'):
	return os.path.join(app(name = 'api'), 'serializers.py')

def permissions(name = 'api'):
	return os.path.join(app(name = 'api'), 'permissions.py')

# FRONTEND
def frontend():
	return os.path.join(super_root(), 'frontend')

def webpack():
	return os.path.join(frontend(), 'webpack.config.js')

def path_manager(query, **kwargs):
	string = ''
	original_query = query
	query = query.lower().replace(' ', '').replace('-', '').replace('_', '').replace('.', '')

	# SUPER ROOT
	if query in ['superroot', 'super']:
		string = super_root()

	# REACTJORC
	elif query in ['reactjorc']:
		string = reactjorc()
	elif query in ['config','cfg','configjson']:
		string = config()
	elif query in ['extensions']:
		string = extensions()
	elif query in ['assets']:
		string = assets(**kwargs)
	elif query in ['helpers', 'helper']:
		string = helpers(**kwargs)
	elif query in ['scaffold', 'scaffolding']:
		string = scaffolding(**kwargs)

	# BACKEND
	elif query in ['backend']:
		string = backend(**kwargs)
	elif query in ['requirements', 'requirementstxt']:
		string = requirements(**kwargs)
	elif query in ['backendproject']:
		string = backend_project()
	elif query in ['manage', 'managepy']:
		string = manage_py()
	elif query in ['settings', 'settingsroot']:
		string = settings()
	elif query in ['settingsbase', 'basesettings']:
		string = os.path.join(settings(), 'base.py')
	elif query in ['settingsdev','settingsdevelopment', 'devsettings','developmentsettings']:
		string = os.path.join(settings(), 'development.py')
	elif query in ['settingsprod','settingsproduction', 'prodsettings', 'productionsettings']:
		string = os.path.join(settings(), 'production.py')
	elif query in ['app']:
		string = app(**kwargs)
	elif query in ['views','viewspy']:
		string = views(**kwargs)
	elif query in ['models','modelspy']:
		string = models(**kwargs)
	elif query in ['urls','urlspy']:
		string = urls(**kwargs)
	elif query in ['admin','adminpy']:
		string = admin(**kwargs)
	elif query in ['tests','testspy']:
		string = tests(**kwargs)
	elif query in ['serializers','serializerspy']:
		string = serializers(**kwargs)
	elif query in ['permissions','permissionspy']:
		string = permissions(**kwargs)

	elif query in ['frontend']:
		string = frontend()
	elif query in ['webpack', 'webpackconfig', 'webpackconfigjs']:
		string = webpack()
	else:
		raise Exception("PATH MANAGER COULDN'T FIND A MATCH FOR: ", original_query)


	return string
