from helpers.config_manager import get_cfg, set_cfg
from helpers.worklist import worklist as wl
from helpers.file_manager import file_manager as f
from helpers.ui import boolean_input
from scaffolding.url import scaffold_url

def scaffold_view():
    if boolean_input('Need a view?'):
        cfg = get_cfg()
        # if 'permissions' in cfg['current_scaffold'].keys():
        #     string = 'permission_classes = ('
        #     string += ', '.join(cfg['current_scaffold']['permissions']) + ','
        #     string += ')'
        # else:
        #     permissions_string = ''

        # Temporarily bypassing permissions until the rest of the system works
        permissions_string = 'permission_classes = [AllowAny]'

        new_view = f('$assets/views/new.py', 'r').format(
            title = cfg['current_scaffold']['model']['title'],
            permissions = permissions_string,
        )
        f('$api/views.py', 'a', new_view)
        print('Created this view:')
        print(' ')
        print(new_view)
        print(' ')

        # Urls only make sense if there is a view. Putting it here.
        scaffold_url()
