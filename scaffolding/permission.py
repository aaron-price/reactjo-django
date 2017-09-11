from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input, options_input
from inflection import pluralize

def scaffold_permission():
    if boolean_input('Add permissions?', 'y'):
        cfg = get_cfg()
        title = cfg['current_scaffold']['model']['title']
        user_types = [
            'Admin', 'Authenticated', 'Anonymous', 'Anybody', 'Nobody'
        ]
        create_type = options_input(
            'Who can create ' + pluralize(title.lower()) + '?',
            user_types, 'Authenticated')

        list_type = options_input(
            'Who can view a list of all ' + pluralize(title.lower()) + '?',
            user_types, 'Anybody')

        detail_type = options_input(
            'Who can view the details about a ' + title.lower() + '?',
            user_types, 'Anybody')

        update_type = options_input(
            'Who can update an existing ' + title.lower() + '?',
            user_types, 'Authenticated')

        delete_type = options_input(
            'Who can delete a ' + title.lower() + '?',
            user_types, 'Authenticated')

        cfg['current_scaffold']['permissions'] = {
            'create': create_type,
            'list': list_type,
            'detail': detail_type,
            'update': update_type,
            'delete': delete_type
        }


        new_permission = f('$assets/permissions/new.py', 'r').format(
            title = title,
            action = 'Create'
        )

        f('$api/permissions.py', 'a', new_permission)
