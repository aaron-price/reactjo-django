from inflection import pluralize

from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input, options_input

def scaffold_permission():
    if boolean_input('Customize permissions?', 'y'):
        cfg = get_cfg()
        title = cfg['current_scaffold']['model']['title']
        user_types = [
            'Superuser', 'Staff', 'Owner', 'Authenticated', 'Anonymous', 'Active', 'Anyone', 'Nobody'
        ]
        post_users = options_input(
            'Who can create ' + pluralize(title.lower()) + '?',
            user_types, 'Authenticated')

        list_users = options_input(
            'Who can view the list of all ' + pluralize(title.lower()) + '?',
            user_types, 'Active')

        details_users = options_input(
            'Who can view the details about a ' + title.lower() + '?',
            user_types, 'Active')

        update_users = options_input(
            'Who can update an existing ' + title.lower() + '?',
            user_types, 'Owner')

        delete_users = options_input(
            'Who can delete an existing ' + title.lower() + '?',
            user_types, 'Owner')

        cfg['current_scaffold']['permissions'] = {
            'post': post_users,
            'list': list_users,
            'details': details_users,
            'update': update_users,
            'delete': delete_users
        }

        new_permission = f('$assets/permissions/new.py', 'r').format(
            Model = title,
            post_users = post_users,
            list_users = list_users,
            details_users = details_users,
            update_users = update_users,
            delete_users = delete_users
        )

        f('$api/permissions.py', 'a', new_permission)
        wl('Created permission')
