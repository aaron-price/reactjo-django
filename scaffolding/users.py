from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input
from helpers.compose import paint
from scaffolding.models import get_model_field, return_model
from scaffolding.permission import scaffold_permission
from helpers.file_manager import file_manager as f
from helpers.worklist import worklist as wl

def quote(string):
    return "'" + string + "'"

def user_permission():
    scaffold_permission()
    f('$api/permissions.py', 'a', '$assets/permissions/post_own_content.py')
    f('$api/permissions.py', 'a', '$assets/permissions/update_own_profile.py')
    wl('Added user permissions')

def scaffold_config():
    cfg = get_cfg()
    cfg['current_scaffold'] = {}
    model = {
        "title": 'UserProfile',
        "fields": [
            {
                "title": "name",
                "type": "CharField",
                "options": [
                    "max_length = 255",
                    "unique = True"
                ],
                "string": "name = models.CharField(max_length=255, unique=True)\n    "
            },
            {
                "title": "email",
                "type": "EmailField",
                "options": [
                    "max_length = 255",
                    "unique = True"
                ],
                "string": "email = models.EmailField(max_length=255, unique=True)\n    "
            }
        ]
    }
    cfg['current_scaffold']['model'] = model
    cfg['current_scaffold']['need_owner'] = 'True'
    set_cfg(cfg)

    print(' ')
    print(' ')
    print(paint(return_model(), 'green'))
    print(' ')
    print(' ')
    if boolean_input('Add some fields to the user model?'):
        get_model_field()

    user_permission()

    # Push current_scaffold to models
    cfg = get_cfg()
    cfg['models'].append(cfg['current_scaffold']['model'])
    set_cfg(cfg)

def user_model_file():
    cfg = get_cfg()
    fields = cfg['current_scaffold']['model']['fields']

    # title_list = ["name", "email", "etc"]
    title_list = [field['title'] for field in fields]

    # quoted_list = ['"name"', '"email"', '"etc"']
    quoted_list = [quote(field['title']) for field in fields]

    # required_list = ['"email"', '"etc"']
    required_list = [field['title'] for field in fields]
    required_list.remove('name')
    required_list = [quote(field) for field in required_list]

    # assignment_list = ["email=email", "name=name"]
    assignment_list = [f'{title}={title}' for title in title_list]

    field_strings = [field['string'] for field in fields]
    model = f('$assets/models/UserProfile.py', 'r').replace(
        'title_list', ', '.join(title_list)).replace(
        'required_list', ', '.join(required_list)).replace(
        'field_strings', ''.join(field_strings)).replace(
        'assignment_list', ', '.join(assignment_list))

    f('$api/models.py', 'a', model)
    wl('Added UserProfile model')

def user_serializers():
    serializer = f('$assets/serializers/user_profile.py', 'r')
    cfg = get_cfg()
    fields = cfg['current_scaffold']['model']['fields']
    titles = [field['title'] for field in fields]
    fields_list = [',\n            ' + quote(t) for t in titles]

    # validated_list = [ name=validated_data['name'], etc ]
    validated_list = [
        f"\n            {t}=validated_data['{t}']," for t in titles
    ]
    serializer = serializer.replace(
        'fields_list', ''.join(fields_list)).replace(
        'validated_list', ''.join(validated_list))
    f('$api/serializers.py', 'a', serializer)
    wl('Added user serializer')

def user_routes():
    # Puts the user routes below the router, but above urlpatterns
    route_flag = '# Register new routes below'
    route_start = f('$api/urls.py','r').find(route_flag)+len(route_flag)+1
    old_urls = f('$api/urls.py', 'r')
    begin = old_urls[:route_start]
    mid = f('$assets/urls/user_urls.py', 'r')
    end = old_urls[route_start:]
    f('$api/urls.py', 'w', begin + mid + end)
    f('$api/urls.py', 'w', '$assets/urls/app_urls_with_users.py')
    wl('Added user routes')

def scaffold_users():
    scaffold_config()
    user_model_file()
    user_serializers()
    user_routes()

    f('$api/views.py', 'a', '$assets/views/users.py')
    f('$api/admin.py', 'a', '$assets/admin/users.py')
