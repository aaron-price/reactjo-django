from tests.config_mock import setup_config, teardown_config
setup_config()

from helpers.path_manager import path_manager as p
import os

def test_paths():
	# SUPER ROOT
	# Aside from super_root, there's also backend_root, and frontend_root below.
	expected = os.getcwd()
	actual = p('super_root')
	assert(expected == actual)

	# REACTJORC
	expected = os.getcwd() + '/reactjorc'
	actual = p('reactjorc')
	assert(expected == actual)

	expected = os.getcwd() + '/reactjorc/config.json'
	actual = p('config')
	assert(expected == actual)

	expected = os.getcwd() + '/reactjorc/extensions'
	actual = p('extensions')
	assert(expected == actual)

	expected = os.getcwd() + '/reactjorc/extensions/django'
	actual = os.path.join(p('extensions'), 'django')
	assert(expected == actual)

	expected = os.getcwd() + '/reactjorc/extensions/django/assets'
	actual = p('assets', name = 'django')
	assert(expected == actual)

	expected = os.getcwd() + '/reactjorc/extensions/django/helpers'
	actual = p('helpers', name = 'django')
	assert(expected == actual)

	expected = os.getcwd() + '/reactjorc/extensions/django/scaffolding'
	actual = p('scaffolding', name = 'django')
	assert(expected == actual)

	# BACKEND
	expected = os.getcwd() + '/backend'
	actual = p('backend')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/requirements.txt'
	actual = p('requirements')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www'
	actual = p('backend_project')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/manage.py'
	actual = p('manage.py')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/www/settings'
	actual = p('settings')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/www/settings/base.py'
	actual = p('settings_base')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/www/settings/development.py'
	actual = p('settings_dev')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/www/settings/production.py'
	actual = p('settings_prod')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/foo'
	actual = p('app', name = 'foo')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/foo/views.py'
	actual = p('views.py', name = 'foo')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/foo/admin.py'
	actual = p('admin.py', name = 'foo')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/foo/models.py'
	actual = p('models.py', name = 'foo')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/foo/urls.py'
	actual = p('urls.py', name = 'foo')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/foo/tests.py'
	actual = p('tests.py', name = 'foo')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/api/serializers.py'
	actual = p('serializers.py')
	assert(expected == actual)

	expected = os.getcwd() + '/backend/www/api/permissions.py'
	actual = p('permissions.py')
	assert(expected == actual)

	# FRONTEND
	expected = os.getcwd() + '/frontend'
	actual = p('frontend')
	assert(expected == actual)

	expected = os.getcwd() + '/frontend/webpack.config.js'
	actual = p('webpack.config.js')
	assert(expected == actual)

	teardown_config()
