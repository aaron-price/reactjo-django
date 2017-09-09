from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f

def scaffold_serializer():
    cfg= get_cfg()
    fields = ''
    for i, field in enumerate(cfg['current_scaffold']['model']['fields']):
        # Get just the title
        title = field.replace('\n', '').replace('\t', '').split(' ')[0]
        if i == 0:
            fields += title
        else:
            fields += ', ' + title

    new_serializer = f('$assets/serializers/new.py', 'r').format(
        Title = cfg['current_scaffold']['model']['Title'],
        fields = fields
    )

    f('$api/serializers.py', 'a', new_serializer)
