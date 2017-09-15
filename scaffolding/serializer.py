from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input

def quote(string):
    return f"'{string}'"

def scaffold_serializer():
    if boolean_input('Need a serializer?', 'y'):
        cfg = get_cfg()
        fields_arr = cfg['current_scaffold']['model']['fields']
        titles = [quote(field['title']) for field in fields_arr]
        fields_str = ', '.join(titles)
        fields_str = "'pk', " + fields_str

        new_serializer = f('$assets/serializers/new.py', 'r').format(
            title = cfg['current_scaffold']['model']['title'],
            fields = fields_str
        )

        f('$api/serializers.py', 'a', new_serializer)
        print('Created this in serializers.py:')
        print(' ')
        print(new_serializer)
        print(' ')
