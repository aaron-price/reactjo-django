from helpers.file_manager import file_manager as f
from helpers.path_manager import path_manager as p
from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input

def user_auth():
    cfg = get_cfg()
    project_name = cfg['project_name']

    need_users = boolean_input('Will users need to signup/login?', 'y')
    cfg['need_users'] = str(need_users)
    set_cfg(cfg)

    if need_users:
        need_posts = boolean_input('Will users be posting their own content?', 'y')
        cfg['need_posts'] = str(need_posts)
        set_cfg(cfg)

        all_settings = [p('base_settings') ,p('dev_settings'), p('prod_settings')]
        for s in all_settings:
            f(s, 'a', "\n\nAUTH_USER_MODEL = 'api.UserProfile'")

        assets = p('assets', 'reactjo_django')
        perm_asset  = f(assets + '/permissions/update_own_profile.py', 'r')
        f(p('permissions', 'api'), 'a', perm_asset)

        serial_asset  = f(assets + '/serializers/user_profile.py', 'r')
        f(p('serializers', 'api'), 'a', serial_asset)

        admin_asset = f(assets + '/admin/users.py', 'r')
        f(p('admin', 'api'), 'a', admin_asset)

        models_asset = f(assets + '/models/UserProfile.py', 'r')
        f(p('models', 'api'), 'a', models_asset)

        views_asset = f(assets + '/views/users.py', 'r')
        f(p('views', 'api'), 'a', views_asset)

        urls_asset = f(assets + '/urls/user_urls.py', 'r')
        data = {
            'target': ['urlpatterns'],
            'content' urls_asset
        }
        f(p('urls', 'api'), 'a', data)

        if need_posts:
            assets = p('assets', 'reactjo_django')
            perm_asset  = f(assets + '/permissions/post_own_content.py', 'r')
            f(p('permissions', 'api'), 'a', perm_asset)
