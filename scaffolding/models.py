from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import string_input, options_input, boolean_input
from helpers.compose import paint
from helpers.compose import quote

types = [
    'AutoField','BigAutoField','BigIntegerField','BinaryField',
    'BooleanField','CharField','CommaSeparatedIntegerField',
    'DateField','DateTimeField','DecimalField','DurationField',
    'EmailField','FileField','FilePathField','FloatField','ImageField',
    'IntegerField','GenericIPAddressField','NullBooleanField',
    'PositiveIntegerField','PositiveSmallIntegerField','SlugField',
    'TextField','TimeField','URLField','UUIDField',
    'ForeignKey','ManyToManyField','OneToOneField'
]
lower_types = [t.lower() for t in types]

# Returns a string showing the model being created so far.
def return_model():
    cfg = get_cfg()
    fields = ''
    for field in cfg['current_scaffold']['model']['fields']:
        fields += field['string']

    new_model = f('$assets/models/new.py', 'r').format(
        title = cfg['current_scaffold']['model']['title'],
        fields = fields,
    )

    if '__str__' in cfg['current_scaffold']['model']:
        str_method = f('$assets/models/str_method.py', 'r').format(
            title = cfg['current_scaffold']['model']['__str__'],
        )
        new_model = new_model + str_method

    if cfg['current_scaffold']['need_owner'] == 'True':
        string = 'def owner_name(self):\n        return self.owner.name\n    '
        new_model = new_model + '\n    ' + string

    return new_model

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
        ml = str(string_input('max_length', '255'))
        field_object['options'].append('max_length = ' + ml)

    # Datefield specific arguments
    if field_type in ['DateField', 'DateTimeField', 'TimeField']:
        # auto_now_add and auto_now cannot be used together.
        auto_now_add = str(boolean_input('Use DateField auto_now_add? '))
        if auto_now_add != 'True':
            auto_now = str(boolean_input('Use DateField auto_now? '))

        # Set the option
        if auto_now_add == 'True':
            field_object['options'].append('auto_now_add = True')
        elif auto_now == 'True':
            field_object['options'].append('auto_now = True')

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
    if field_type in ['FilePathField']:
        path = string_input('path = ')
        field_object['options'].append('path = ' + quote(path))

        match = string_input("match. For example r'$^'", None)
        if match != None:
            field_object['options'].append('match = ' + match)

        max_length = string_input('max_length', None)
        if max_length != None:
            field_object['options'].append('max_length = ' + max_length)

        recursive = str(boolean_input('recursive', 'n'))
        field_object['options'].append('recursive = ' + recursive)

        allow_files = str(boolean_input('allow_files', 'y'))
        field_object['options'].append('allow_files = ' + allow_files)

        allow_folders = str(boolean_input('allow_folders', 'n'))
        field_object['options'].append('allow_folders = ' + allow_folders)

    if field_type == 'ImageField':
        height_field = string_input('height_field', None)
        if height_field != None:
            field_object['options'].append('height_field = ' + height_field)

        width_field = string_input('width_field', None)
        if width_field != None:
            field_object['options'].append('width_field = ' + width_field)

    if field_type == 'SlugField':
        max_length = string_input('max_length', '50')
        field_object['options'].append('max_length = ' + max_length)

    if field_type == 'URLField':
        max_length = string_input('max_length', '200')
        field_object['options'].append('max_length = ' + max_length)

    foreign = False
    if field_type in ['ForeignKey', 'OneToOneField', 'ManyToManyField']:
        models = [model['title'] for model in cfg['models']]
        models.append('self')
        other_model = options_input('Choose a foreign model', models)
        field_object['options'].append(quote(other_model))

        if boolean_input('Add a related_name option?', 'n'):
            related_name = string_input(
                'related_name =',
                cfg['current_scaffold']['model']['title'].lower()
            )
            field_object['options'].append('related_name = ' + quote(related_name))

    if field_type in ['ForeignKey', 'OneToOneField']:
        choices = [
            'CASCADE', 'PROTECT', 'SET_NULL',
            'SET_DEFAULT','SET()','DO_NOTHING'
        ]
        on_delete = options_input('on_delete ', choices, 'CASCADE')
        field_object['options'].append('on_delete = models.' + on_delete)

    # If we missed anything, let the user add it now.
    def more_options():
        if boolean_input(
            'Add another option to' + field_object['title'] + '?',
            'n'):
            new_option = string_input("enter it now. (e.g. foo='bar')")
            field_object['options'].append(new_option)
            more_options()

    # Build the string
    ftitle = field_object['title']
    ftype = field_object['type']
    foptions = ''
    for i, o in enumerate(field_object['options']):
        if i > 0:
            foptions += f', {o}'
        else:
            foptions = o
    cfg['current_scaffold']['model']['fields'].append({
        'title': ftitle,
        'type': ftype,
        'options': field_object['options'],
        'string': f'{ftitle} = models.{ftype}({foptions})\n    '
    })

    set_cfg(cfg)
    print('========================')
    print('Your model so far:')
    print(' ')
    print(paint(return_model(), 'green'))
    print('========================')

    another_field = boolean_input('Make another field? ')
    if another_field:
        get_model_field()

    # All done making fields.
    # Add the __str__ method
    else :
        user = cfg['current_scaffold']['model']['title'] == 'UserProfile'
        if not user:
            current_fields = cfg['current_scaffold']['model']['fields']
            titles = [field['title'] for field in current_fields]
            default_title = titles[0]
            if cfg['current_scaffold']['need_owner'] == 'True':
                default_title = titles[1]

            str_field = options_input(
                'Which field should be used for the __str__ method?',
                titles,
                default_title
            )

            cfg['current_scaffold']['model']['__str__'] = str_field
            set_cfg(cfg)

def scaffold_model():
    cfg = get_cfg()
    # Add title
    title = string_input('What will you call your model? ').capitalize()
    cfg['current_scaffold']['model']['title'] = title
    cfg['current_scaffold']['model']['fields'] = []
    set_cfg(cfg)

    # Should never be necessary, but just in case.
    if 'models' not in cfg:
        cfg['models'] = []
        set_cfg(cfg)

    # Add owner field if necessary
    need_owner = False
    if cfg['need_users']:
        need_owner = boolean_input('Will users own instances of this model?')
    if need_owner:
        cfg['current_scaffold']['model']['fields'].append({
            'title': 'owner',
            'type': 'ForeignKey',
            'options': ['UserProfile', 'on_delete = models.CASCADE'],
            'string': f"owner = models.ForeignKey('UserProfile', on_delete = models.CASCADE)\n    "
        })

        cfg['current_scaffold']['need_owner'] = 'True'
    else:
        cfg['current_scaffold']['need_owner'] = 'False'
    set_cfg(cfg)

    # Add other fields
    print(' ')
    print('Let\'s create at least one model field now.')
    get_model_field()

    # Refresh config
    cfg = get_cfg()

    # Put the model in models.py
    f('$api/models.py', 'a', return_model())
    wl('Created the ' + title + ' model')

    # Put the model in config.json
    fields = cfg['current_scaffold']['model']['fields']
    title = cfg['current_scaffold']['model']['title']
    str_method = cfg['current_scaffold']['model']['__str__']
    cfg['models'].append({
        'title': title,
        'fields': fields,
        '__str__': str(str_method),
    })
    set_cfg(cfg)
