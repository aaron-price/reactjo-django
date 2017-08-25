from helpers.cli import manage, startapp
from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p
from helpers.config_manager import get_cfg, set_cfg
from scaffolding.update_settings import new_app_settings

def new_app(name):
    startapp(name)
    new_app_settings(name)

    cfg = get_cfg()
    assets_path = p('assets', name='reactjo_django')
    app_path = p('app', name=name)
    project_path = p('backend_project')
    project_name = cfg['project_name']

    # NEW ENTRY IN ROOT URLS
    new_url_entry = f(assets_path + '/urls/new_root_url.py','f', {'name': name})
    data = {
        'target': ['urlpatterns'],
        'content': '\n\t' + new_url_entry
    }
    f(p('urls', name=project_name), 'a', data)

    # PREPARE FILES IN APP DIR
    admin_asset = f(assets_path + '/admin/imports.py', 'r')
    f(p('admin.py', name=name), 'w', admin_asset)

    serial_asset = f(assets_path + '/serializers/imports.py', 'r')
    f(p('serializers.py', name=name), 'w', serial_asset)

    permissions_asset = f(assets_path + '/permissions/imports.py', 'r')
    f(p('permissions.py', name=name), 'w', permissions_asset)

    views_asset = f(assets_path + '/views/imports.py', 'r')
    f(p('views.py', name=name), 'w', views_asset)

    models_asset = f(assets_path + '/models/imports.py', 'r')
    f(p('models.py', name=name), 'w', models_asset)

    urls_asset = f(assets_path + '/urls/base_app_url.py', 'r')
    f(p('urls.py', name=name), 'w', urls_asset)
