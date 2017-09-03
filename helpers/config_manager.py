import subprocess
import os
import json

checked = []

# JSON functions duplicated here to avoid circular imports with file_manager
def json_read(path):
    with open(path, 'r') as file:
        return json.load(file)

def json_write(path, content):
    with open(path, 'w') as file:
        json.dump(content, file, indent = 4)

def find_config_path():
    def check():
        # reactjo.json exists?
        config_file = os.path.isfile('./reactjorc/config.json')
        checked.append(os.getcwd())
        return found() if config_file else bubble_up(os.getcwd())

    def bubble_up(prev_path):
        os.chdir("..")
        next_path = os.getcwd()
        # Escape the recursion if "cd .." does nothing.
        raise Exception() if prev_path == next_path else check()

    def found():
        return os.getcwd() + '/reactjorc/config.json'

    return check()

def get_cfg():
    try:
        return json_read(find_config_path())
    except:
        print("""
            Sorry, couldn't find the config.json file. cd to that directory,
            or a child directory. If there really is no config.json, you
            probably need to create a project. Try running:
                        ----------------------
                            reactjo init
                        ----------------------
            Paths checked for a reactjorc/config.json:
        """)
        for path in checked:
            print(path)

def set_cfg(content):
    json_write(find_config_path(), content)
