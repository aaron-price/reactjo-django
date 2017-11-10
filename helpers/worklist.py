from helpers.config_manager import get_cfg, set_cfg
import os
def worklist(string, prev_path = None):
    # Solves issues with finding config.json after changing dirs
    if prev_path:
        next_path = os.getcwd()
        os.chdir(prev_path)

    cfg = get_cfg()

    # Create worklist if necessary. Should never be necessary.
    if not 'worklist' in cfg:
        cfg['worklist'] = []

    # Add worklist entry
    cfg['worklist'].append(string)
    set_cfg(cfg)

    if prev_path:
        os.chdir(next_path)
