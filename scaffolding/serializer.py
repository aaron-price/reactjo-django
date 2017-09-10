from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input

def quote(string):
    return f"'{string}'"

def scaffold_serializer():
    if boolean_input('Need a serializer?'):
        cfg= get_cfg()
        fields = ''
        for i, field in enumerate(cfg['current_scaffold']['model']['fields']):
            # Get just the title
            title = field.replace('\n', '').replace('\t', '').split(' ')[0]
            fields += quote(title) + ', '

        new_serializer = f('$assets/serializers/new.py', 'r').format(
            title = cfg['current_scaffold']['model']['title'],
            fields = fields
        )

        f('$api/serializers.py', 'a', new_serializer)
