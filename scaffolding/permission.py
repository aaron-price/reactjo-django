from inflection import pluralize

from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input, options_input

def quote(string):
    return "'" + string + "'"

def scaffold_permission():
    cfg = get_cfg()
    title = cfg['current_scaffold']['model']['title']
    model = 'User' if title == 'UserProfile' else title

    if boolean_input('Customize permissions for ' + model + '?', 'y'):
        all_types = [
            'Superuser',
            'Staff',
            'Authenticated',
            'Anonymous',
            'Active',
            'Anyone',
            'Nobody',
            'Owner'
        ]
        without_owner = all_types[:-1]
        with_owner = all_types[:-1]
        default_update = 'Staff'
        default_delete = 'Staff'

        if cfg['current_scaffold']['need_owner'] == 'True':
            with_owner = all_types
            default_update = 'Owner'
            default_delete = 'Owner'

        is_user = title == 'UserProfile'
        default_post = 'Anonymous' if is_user else 'Authenticated'
        post_users = options_input(
            'Who can create ' + pluralize(title.lower()) + '?',
            without_owner, default_post)

        list_users = options_input(
            'Who can view the list of all ' + pluralize(title.lower()) + '?',
            without_owner, 'Anyone')

        details_users = options_input(
            'Who can view the details about a ' + title.lower() + '?',
            with_owner, 'Anyone')

        update_users = options_input(
            'Who can update an existing ' + title.lower() + '?',
            with_owner, 'Owner')

        delete_users = options_input(
            'Who can delete an existing ' + title.lower() + '?',
            with_owner, 'Owner')

        cfg['current_scaffold']['permissions'] = {
            'post': post_users,
            'list': list_users,
            'details': details_users,
            'update': update_users,
            'delete': delete_users
        }
        set_cfg(cfg)


        new_permission = f('$assets/permissions/new.py', 'r').format(
            Model = model,
            post_users = quote(post_users),
            list_users = quote(list_users),
            details_users = quote(details_users),
            update_users = quote(update_users),
            delete_users = quote(delete_users)
        )

        f('$api/permissions.py', 'a', new_permission)
        wl('Created permission')
    else:
        default_update = 'Staff'
        default_delete = 'Staff'
        if cfg['current_scaffold']['need_owner'] == 'True':
            default_update = 'Owner'
            default_delete = 'Owner'
        default_post = 'Anonymous' if model == 'User' else 'Authenticated'

        cfg['current_scaffold']['permissions'] = {
            'post': default_post,
            'list': 'Anyone',
            'details': 'Anyone',
            'update': default_update,
            'delete': default_delete
        }
        set_cfg(cfg)

        new_permission = f('$assets/permissions/new.py', 'r').format(
            Model = model,
            post_users = quote(default_post),
            list_users = quote('Anyone'),
            details_users = quote('Anyone'),
            update_users = quote(default_update),
            delete_users = quote(default_delete)
        )

        f('$api/permissions.py', 'a', new_permission)
        wl('Created permission')
