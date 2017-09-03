from helpers.data_detection import get_brackets, get_variable, get_string_contents, get_type, list_index_positions, detect_duplicate
from helpers.commas import soft_comma
import os
from helpers.file_manager import file_manager
from tests.config_mock import setup_config, teardown_config

def debug_print(e, a):
    print("EXPECTED")
    print(e)
    print("ACTUAL")
    print(a)

def test_get_string_contents():
    setup_config()
    string = "foo = 'hello!'"
    assert(get_string_contents(string, 0) == "'hello!'")

def test_get_variable():
    file = file_manager('tests/sandbox/settings.py', 'r')
    data = {
        'target': ['thing']
    }
    var = get_variable(file, data)
    print(var)
    assert(var['string'] == 'thing = "hello"')

def test_get_type():
	string = "config = { 'foo': 1 }"
	types = get_type(string)
	assert(types['typ'] == '{')
	assert(types['opposite'] == '}')

	string = "config = { 'foo': 1, bar: [2,3,4] }"
	types = get_type(string)
	assert(types['typ'] == '{')
	assert(types['opposite'] == '}')

	string = "config = [ 2,3,3 ]"
	types = get_type(string)
	assert(types['typ'] == '[')
	assert(types['opposite'] == ']')

	string = "config = [ {'foo': 1}, 2,3,3 ]"
	types = get_type(string)
	assert(types['typ'] == '[')
	assert(types['opposite'] == ']')

def test_finds_closing_bracket():
	file = file_manager('tests/sandbox/settings.py', 'read')
	actual = get_brackets(file, file.find('config'))

	assert(actual['start'] == 194)
	assert(actual['stop'] == 343)

def test_finds_opening_bracket():
	file = file_manager('tests/sandbox/settings.py', 'read')
	actual = get_brackets(file, file.find('INSTALLED_APPS'))

	assert(actual['start'] == 50)


def test_finds_list_indices():
	# Should include all commas that are not inside of strings, or nested children
	string = "foo = [1,2,'hello, world',{'bar': 1, 'cats': 2},'lol']"
	indices = list_index_positions(string, 0, len(string) - 1)
	expected = [7,9,11,26,48]

	debug_print(expected, indices)
	assert(indices == expected)

def test_soft_comma():
	# Should add commas and a space if necessary, remove if unnecessary.
	item1 = 'foo'
	item2 = 'bar'
	output = soft_comma(item1, item2)
	assert(output == 'foo, bar')

	item1 = 'foo,'
	item2 = 'bar'
	output = soft_comma(item1, item2)
	assert(output == 'foo, bar')

	item1 = 'foo,'
	item2 = ',bar'
	output = soft_comma(item1, item2)
	assert(output == 'foo, bar')

def test_detect_duplicate():
	content = 'foo'
	target = 'stuff = ["bar", "foo": 123]'
	assert(detect_duplicate(target, content) == True)

	content = 'foo'
	target = 'stuff = ["bar", "baz": 123]'
	assert(detect_duplicate(target, content) == False)

	content = 'foo,'
	target = 'stuff = ["bar", "foo": 123]'
	assert(detect_duplicate(target, content) == True)

	content = '"foo"'
	target = 'stuff = ["bar", "foo"]'
	assert(detect_duplicate(target, content) == True)

	content = 'foo'
	target = 'stuff = ["bar", "foo"]'
	assert(detect_duplicate(target, content) == True)
