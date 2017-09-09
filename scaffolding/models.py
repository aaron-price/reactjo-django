from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import string_input, options_input, boolean_input
types = [
    'AutoField', 'BigAutoField', 'BigIntegerField', 'BinaryField',
    'BooleanField', 'CharField', 'CommaSeparatedIntegerField',
    'DateField','DecimalField','DurationField','EmailField',
    'FileField','FilePathField','FloatField','ImageField',
    'IntegerField','GenericIPAddressField','NullBooleanField',
    'PositiveIntegerField','PositiveSmallIntegerField','SlugField',
    'TextField','TimeField','URLField','UUIDField','ForeignKey'
]
lower_types = [t.lower() for t in types]

def return_model():
    cfg = get_cfg()
    fields = ''
    for field in cfg['current_scaffold']['model']['fields']:
        fields += field

    new_model = f('$assets/models/new.py', 'r').format(
        Title = cfg['current_scaffold']['model']['Title'],
        fields = fields
    )
    return new_model


def quote(string):
	return "''{}'".format(string)

def get_model_field():
    cfg = get_cfg()
    field_title = string_input('Name this field')
    field_type = options_input('Which fieldtype would you like to use? ', types)

    # Get correct option, regardless of caps
    field_type = types[lower_types.index(field_type.lower())]
    field_object = {
        'title': field_title,
        'type': field_type,
        'options': [],
    }

    if field_type in ['CharField', 'CommaSeparatedIntegerField', 'EmailField']:
        ml = string_input('max_length', 255)
        field_object['options'].append('max_length = ' + ml)

    # Datefield specific arguments
    if field_type in ['DateField', 'TimeField']:
        auto_now = boolean_input('Use DateField auto_now? ')
        auto_now_add = boolean_input('Use DateField auto_now_add? ')

        field_object['options'].append('auto_now = ' + auto_now)
        field_object['options'].append('auto_now_add = ' + auto_now_add)

    # Decimalfield specific arguments
    if field_type == 'DecimalField':
        decimal_places = string_input('decimal_places')
        max_digits = string_input('max_digits')
        field_object['options'].append('decimal_places = ' + decimal_places)
        field_object['options'].append('max_digits = ' + max_digits)

    # Filefield specific arguments
    if field_type == 'FileField':
        upload_to = string_input('upload_to', None)
        if upload_to != None:
            field_object['options'].append('upload_to = ' + quote(upload_to))

        storage = string_input('storage', None)
        if storage != None:
            field_object['options'].append('storage = ' + quote(storage))

        max_length = string_input('max_length', None)
        if max_length != None:
            field_object['options'].append('max_length = ' + max_length)

    # FilePathField specific arguments
    if field_type in ['FilePathField', 'ImageField']:
        path = string_input('path = ')
        field_object['options'].append('path = ' + quote(path))

        match = string_input("match. For example r'$^'", None)
        if match != None:
            field_object['options'].append('match = ' + match)

        max_length = string_input('max_length', None)
        if max_length != None:
            field_object['options'].append('max_length = ' + max_length)

        recursive = boolean_input('recursive', 'n')
        field_object['options'].append('recursive = ' + recursive)

        allow_files = boolean_input('allow_files', 'y')
        field_object['options'].append('allow_files = ' + allow_files)

        allow_folders = boolean_input('allow_folders', 'n')
        field_object['options'].append('allow_folders = ' + allow_folders)

    if field_type == 'ImageField':
        height_field = string_input('height_field', None)
        if height_field != None:
            field_object['options'].append('height_field = ' + height_field)

        width_field = string_input('width_field', None)
        if width_field != None:
            field_object['options'].append('width_field = ' + width_field)

    if field_type == 'SlugField':
        max_length = string_input('max_length', 50)
        field_object['options'].append('max_length = ' + max_length)

    if field_type == 'URLField':
        max_length = string_input('max_length', 200)
        field_object['options'].append('max_length = ' + max_length)

    foreign = False
    if field_type == 'ForeignKey':
        models = [model['title'] for model in cfg['models']]
        models.append('self')
        other_model = options_input('Choose a foreign model', models)
        field_object['options'].append(quote(other_model))

        choices = [
            'CASCADE', 'PROTECT', 'SET_NULL',
            'SET_DEFAULT','SET()','DO_NOTHING'
        ]
        on_delete = options_input('on_delete', choices, 'CASCADE')
        field_object['options'].append('on_delete = ' + quote(on_delete))

    # Build the string
    ftitle = field_object['title']
    ftype = field_object['type']
    foptions = ''
    for i, o in enumerate(field_object['options']):
        if i > 0:
            foptions += f', {o}'
        else:
            foptions = o
    cfg['current_scaffold']['model']['fields'].append(
        f'{ftitle} = models.{ftype}({foptions})\n\t'
    )
    set_cfg(cfg)
    print(return_model())

    another_field = boolean_input('Make another field? ')
    if another_field:
        get_model_field()

def scaffold_model():
    cfg = get_cfg()
    Title = string_input('What will you call your model? ')
    cfg['current_scaffold']['model']['Title'] = Title
    cfg['current_scaffold']['model']['fields'] = []
    set_cfg(cfg)

    if boolean_input(f'Create a field for {Title}? '):
        get_model_field()

    f('$api/models.py', 'a', return_model())
