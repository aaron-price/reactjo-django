import subprocess
import os
import json
from textwrap import dedent

# JSON functions duplicated here to avoid circular imports with file_manager
def json_read(path):
    with open(path, 'r') as file:
        return json.load(file)

def json_write(path, content):
    with open(path, 'w') as file:
        json.dump(content, file, indent = 4)

checked = []
current_path = os.getcwd()


def find_config_path():
    def check():
        # reactjo.json exists?
        cfg_path = os.path.join(current_path, 'reactjorc/config.json')
        config_file = os.path.isfile(cfg_path)
        checked.append(os.getcwd())
        return found() if config_file else bubble_up()

    def bubble_up():
        parent_path = os.path.dirname(current_path)
        # Escape the recursion if already at highest level.
        if current_path == parent_path:
            raise Exception()
        else:
            current_path = parent_path
            check()

    def found():
        checked = []
        return os.path.join(current_path, 'reactjorc/config.json')

    return check()

def get_cfg():
    try:
        return json_read(find_config_path())
    except:
        print(dedent("""
            Sorry, couldn't find the config.json file. cd to that directory,
            or a child directory. If there really is no config.json, you
            probably need to create a project. Try running:
                        ----------------------
                            reactjo rc
                        ----------------------
            Paths checked for a reactjorc/config.json:
        """))
        for path in checked:
            print(path)

def set_cfg(content):
    json_write(find_config_path(), content)
