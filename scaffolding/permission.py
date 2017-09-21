from inflection import pluralize

from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input, options_input

def scaffold_permission():
    cfg = get_cfg()
    # Get data
    title = cfg['current_scaffold']['model']['title']
    model = 'User' if title == 'UserProfile' else title
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
    ownerless = all_types[:-1]
    custom = boolean_input('Customize permissions for ' + model + '?', 'y')
    auth = cfg['need_users'] == 'True'
    owner = cfg['current_scaffold']['need_owner'] == 'True'

    # Adjust data
    if not auth:
        all_types.remove('Authenticated')
        all_types.remove('Staff')
    if not owner:
        all_types.remove('Owner')

    # Build the questions
    list_answer = 'Anyone'
    list_options = ownerless
    list_q = 'Who can view the list of all ' + pluralize(model.lower()) + '?'

    details_answer = 'Anyone'
    details_options = all_types
    details_q = 'Who can view the details of a ' + model.lower() + '?'

    post_answer = 'Authenticated'
    post_options = ownerless
    post_q = 'Who can create a ' + model.lower() + '?'

    update_answer = 'Owner'
    update_options = all_types
    update_q = 'Who can update an existing ' + model.lower() + '?'

    delete_answer = 'Owner'
    delete_options = all_types
    delete_q = 'Who can delete an existing ' + model.lower() + '?'

    # Ask questions if necessary
    if custom:
        list_answer = options_input(list_q, ownerless, list_answer)
        details_answer = options_input(details_q, ownerless, details_answer)
        post_answer = options_input(post_q, ownerless, post_answer)
        update_answer = options_input(update_q, ownerless, update_answer)
        delete_answer = options_input(delete_q, ownerless, delete_answer)

    # Update config
    cfg['current_scaffold']['permissions'] = {
        'list': list_answer,
        'details': details_answer,
        'post': post_answer,
        'update': update_answer,
        'delete': delete_answer,
    }
    set_cfg(cfg)

    # Build permisionset
    new_permission = f('$assets/permissions/new.py', 'r').format(
        Model = model,
        list_users = list_answer,
        details_users = details_answer,
        post_users = post_answer,
        update_users = update_answer,
        delete_users = delete_answer,
    )
    f('$api/permissions.py', 'a', new_permission)
    wl('Created permission')
