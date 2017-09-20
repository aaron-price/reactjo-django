from helpers.config_manager import get_cfg, set_cfg
from helpers.ui import boolean_input
from scaffolding.models import get_model_field, return_model
from scaffolding.permission import scaffold_permission

def scaffold_config():
    cfg = get_cfg()
    cfg['current_scaffold'] = {}
    model = {
        "title": 'UserProfile',
        "fields": [
            {
                "title": "email",
                "type": "EmailField",
                "options": [
                    "max_length = 255",
                    "unique = True"
                ],
                "string": "email = models.EmailField(max_length=255, unique=True)\n    "
            },
            {
                "title": "name",
                "type": "CharField",
                "options": [
                    "max_length = 255",
                    "unique = True"
                ],
                "string": "name = models.CharField(max_length=255, unique=True)\n    "
            }
        ]
    }
    cfg['current_scaffold']['model'] = model
    cfg['current_scaffold']['need_owner'] = 'True'
    set_cfg(cfg)
    return_model()

    if boolean_input('Add some fields to the user model?'):
        get_model_field()

    scaffold_permission()

def scaffold_files():
    cfg = get_cfg()

def scaffold_users():
    scaffold_config()
    scaffold_files()
