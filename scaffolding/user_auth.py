from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input

def user_auth():
    pass
    # cfg = get_cfg()
    # project_name = cfg['project_name']
    #
    # need_users = boolean_input('Will users need to signup/login?', 'y')
    # cfg['need_users'] = "True" if need_users else "False"
    # set_cfg(cfg)
    #
    # if need_users:
    #     all_settings = [p('base_settings') ,p('dev_settings'), p('prod_settings')]
    #     for s in all_settings:
    #         f(s, 'a', "\n\nAUTH_USER_MODEL = 'profiles_api.UserProfile'")
    #
    #     perm_asset  = f(p('assets', 'reactjo_django') + '/permissions.py', 'r')
    #     f(p('permissions', 'api'), 'w', perm_asset)
    #
    #     serial_asset  = f(p('assets', 'reactjo_django') + '/serializers.py', 'r')
    #     f(p('serializers', 'api'), 'w', serial_asset)
    #
    #     views_asset = f(p('assets', 'reactjo_django') + '/views.py', 'r')
    #     f(p('views', 'api'), 'w', views_asset)
    #
    #     urls_asset = f(p('assets', 'reactjo_django') + '/urls.py', 'r')
    #     f(p('urls', 'api'), 'w', urls_asset)
    #
    #     admin_asset = f(p('assets', 'reactjo_django') + '/admin.py', 'r')
    #     f(p('admin', 'api'), 'w', admin_asset)
    #
    #     models_asset = f(p('assets', 'reactjo_django') + '/models.py', 'r')
    #     f(p('models', 'api'), 'w', models_asset)
    #
    # root_urls_asset = f(p('assets', 'reactjo_django') + '/root_urls.py', 'r')
    # f(p('urls', project_name), 'w', urls_asset)
