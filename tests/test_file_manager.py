import os
from helpers.file_manager import file_manager

good_path = 'tests/sandbox/exists'
bad_path = 'tests/nope/wrong'
good_file = 'tests/sandbox/exists/blank.txt'
bad_file = 'tests/sandbox/exists/wrong.txt'
new_file = 'tests/sandbox/foo.txt'
settings_file = 'tests/sandbox/settings.py'
settings_config = 'tests/sandbox/settings_config.py'
settings_config_more = 'tests/sandbox/settings_config_more.py'
settings_appended = 'tests/sandbox/settings_appended.py'
settings_kittens = 'tests/sandbox/settings_kittens.py'
new_settings = 'tests/sandbox/new_settings.py'
settings_custom = 'tests/sandbox/settings_config_custom.py'



# Check existence.
def test_file_manager_existance():
    assert(file_manager(good_path, 'exists') == True)
    assert(file_manager(bad_path, 'exists') == False)
    assert(file_manager(good_file, 'exists') == True)
    assert(file_manager(bad_file, 'exists') == False)

# Check a path
def test_file_manager_path():
    actual = file_manager('$prj/backend/foo/bar', 'path')
    expected = os.getcwd() + '/www/backend/foo/bar'
    assert(actual == expected)

# Writing
def test_file_manager_writing():
    contents = 'Hello world!'
    assert(file_manager(new_file, 'exists') == False)
    file_manager(new_file, 'write', contents)
    assert(file_manager(new_file, 'exists') == True)

def test_file_write_from_path():
    src = '$su/tests/sandbox/write_from_src.txt'
    target = '$su/tests/sandbox/write_from_target.txt'
    file_manager(target, 'w', src)

    actual = file_manager(target, 'r')
    expected = 'Hello World\n'
    assert(actual == expected)

def test_file_manager_line_remove():
    settings = file_manager(settings_file, 'r')
    overwritable_path = 'tests/sandbox/overwrite_me.py'
    file_manager(overwritable_path, 'w', settings)
    data = {
        'target': 'world =',
        'content': ''
    }
    file_manager(overwritable_path, 'w', data)
    actual = file_manager(overwritable_path, 'r')
    expected = file_manager('tests/sandbox/expected_string_remove.py', 'r')
    assert(actual == expected)

def test_file_manager_line_overwrite():
    settings = file_manager(settings_file, 'r')
    overwritable_path = 'tests/sandbox/overwrite_me.py'
    file_manager(overwritable_path, 'w', settings)
    data = {
        'target': 'world =',
        'content': 'world = "Mars"'
    }
    file_manager(overwritable_path, 'w', data)
    actual = file_manager(overwritable_path, 'r')
    expected = file_manager('tests/sandbox/expected_overwrite_string.py', 'r')
    assert(actual == expected)

# Reading
def test_file_manager_reading():
    actual   = file_manager(settings_file, 'r')
    expected = open(settings_file, 'r').read()
    assert(actual == expected)

    actual   = file_manager(settings_file, 'r', ['config'])
    expected = file_manager(settings_config, 'r')
    assert(actual == expected)

    actual   = file_manager(settings_file, 'r', ['config','more'])
    expected = file_manager(settings_config_more, 'r')
    assert(actual == expected)

# Appending - Simple EOF
def test_file_manager_EOF_append():
    file_manager(new_file, 'w', "Hello")
    file_manager(new_file, 'a', "World")
    file = file_manager(new_file, 'r')

    assert(file == "Hello\nWorld")

# Appending - inside of nested lists
def test_file_manager_list_append():
    list_append_file = 'tests/sandbox/list_append.py'
    settings = file_manager(settings_file, 'r')
    file_manager(list_append_file, 'w', settings)

    data = {
        'target': ['config', 'more'],
        'content': ",\n        'kittens'"
    }
    file_manager(list_append_file, 'a', data)

    expected = file_manager(settings_kittens, 'r')
    actual   = file_manager(list_append_file, 'r')
    assert(expected == actual)

    # Duplicate entries should be ignored
    data = {
        'target': ['config', 'more'],
        'content': ",\n        'kittens'"
    }
    file_manager(list_append_file, 'a', data)

    expected = file_manager(settings_kittens, 'r')
    actual   = file_manager(list_append_file, 'r')
    assert(expected == actual)

    # extra or missing commas shouldn't be an issue
    # Reset list_append_file
    file_manager(list_append_file, 'w', settings)
    data = {
        'target': ['config', 'more'],
        'content': "\n        'kittens'"
    }
    file_manager(list_append_file, 'a', data)

    expected = file_manager(settings_kittens, 'r')
    actual   = file_manager(list_append_file, 'r')
    assert(expected == actual)

# Appending - inside of nested dicts
def test_file_manager_dict_append():
    dict_append_file = 'tests/sandbox/dict_append.py'
    dict_append_expected = 'tests/sandbox/dict_append_expected.py'
    settings = file_manager(settings_file, 'r')
    file_manager(dict_append_file, 'w', settings)

    data = {
        'target': ['config', 'more', 1],
        'content': "\n            'custom': 'something custom'"
    }
    file_manager(dict_append_file, 'a', data)

    expected = file_manager(dict_append_expected, 'r')
    actual   = file_manager(dict_append_file, 'r')
    assert(expected == actual)

def test_file_manager_prepend():
    actual_path = 'tests/sandbox/prepend_list_actual.py'
    expected_path = 'tests/sandbox/prepend_list_expected.py'
    working_file = file_manager(settings_file, 'r')
    file_manager(actual_path, 'w', working_file)

    data = {
        'target': ['INSTALLED_APPS'],
        'content': "\n    'cat'"
    }
    file_manager(actual_path, 'p', data)

    expected = file_manager(expected_path, 'r')
    actual = file_manager(actual_path, 'r')
    assert(expected == actual)

# Parsing templates
def test_file_manager_templating():
    basic_component     = 'tests/sandbox/basic_component.js'
    parsed_component    = 'tests/sandbox/parsed_component.js'
    expected_parsed_component = 'tests/sandbox/expected_parsed_component.js'
    data = {'app_name': 'Fooness','model_name': 'Bar'}
    component = file_manager(basic_component, 'f', data)

    file_manager(parsed_component, 'w', component)

    expected = file_manager(expected_parsed_component, 'r')
    actual   = file_manager(parsed_component, 'r')
    assert(actual == expected)

# Removing (keep at the bottom)
def test_file_manager_removing():
    file_manager(new_file, 'remove')
    assert(file_manager(new_file, 'exists') == False)
