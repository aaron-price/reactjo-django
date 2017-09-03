# If you want to create a new extension
## Create and publish


1. Clone the template
```bash
reactjo extend
# Name the extension
cd extension_name
```
(Note if you directly cloned it yourself, you'll need to edit ./helpers/extension_constants.py)
But reactjo extend does this automatically.

2. Make some changes.
3. Update this README.md.
  3a. Update the github uri in the json object below.
  3b. Document the commands you use under # Usage
4. Push the extension to a new github repo matching the uri you specified in 3a.

That's it! People can now use it as a Reactjo extension by adding that object to their config.json extensions array.

## Commands

To listen to a new reactjo command, edit django_trial/entry.py.
You should probably add a module for the command under django_trial/commands/

## Helpers
#### file_manager

File manager automatically uses the path_manager helper. Use this for super simple file manipulation.
For example to copy your foobar.txt asset into your main output directory:
```
from helpers.file_manager import file_manager as f
f('$out/foobar.txt', 'w', '$assets/foobar.txt')
```
As you can see the basic syntax is f(output path, query type, input path or data dictionary).
The $out and $assets are shortcuts courtesy of helpers/path_manager.py. Check it out to see more.
So in this case, it's saying "In the output file, write the input file."

Some other queries are:
append: f(path, 'a', <string|dict>)
exists: f(path, 'exists')
write: f(path, 'w', <string|dict>)
delete: f(path, 'd', <string>)
prepend: f(path, 'p', <string|dict>)
read: f(path, 'r')
format: f(path, 'f', <dict>) *

* Formatting: Wrap text like <% this %>, and you can replace it... because python's string.format() doesn't work as well when formatting python files with existing dicts. Takes a dict input like {'this': 'something else'}

It gets crazier than that though! If your input is a dictionary, you can do some pretty advanced manipulations.

Example:

```settings.py
OPTIONS = {
  'cool': 124,
  'my_list': [
    'asdfasdf',
    {
      'foo': {...}      # <- You need a new entry below foo
    }
  ]
}
```

You *could* just add an append line at the bottom of the file, but that doesn't look nice, especially in a settings or config file. Here's a better solution.

```

data = {
      'target': ['OPTIONS', 'my_list', 1],
      'content': "\n      'custom': 'something custom'"
  }
  f($out/settings.py, 'a', data)
```

New file will be:

```settings.py
OPTIONS = {
  'cool': 124,
  'my_list': [
    'asdfasdf',
    {
      'foo': {...},
      'custom': 'something custom'
    }
  ]
}
```

Note the comma was added automatically. You might not know whether a trailing comma exists, so file_manager checks for you and adds it if necessary. You do need to add your own newline and indentation though.

You're also not limited to a particular filetype. The same would work in settings.js etc.

#### config_manager
Intelligently finds the nearest reactjorc/config.json file so you can access it from pretty much anywhere super_root level or deeper.

```python
from helpers.config_manager import get_cfg, set_cfg
# loads the config file as a dict
cfg = get_cfg()

cfg['new_key'] = 'new value'
project_name = cfg['project_name']

# Updates the config file. This may affect other extensions, so be careful.
set_cfg(cfg)
```

#### ui
Provides type specific inputs.
The first argument is the question to ask the end user.

Adding a secondary argument makes it optional, and uses the second argument as the default.

The exception is the options_input which takes a list of options as the second argument, and the optional default as the third.

```python
from helpers.ui import string_input, boolean_input, options_input
# prints What's your name?:
mandatory_string = string_input('What\'s your name?')

# prints 'What's the best colour ever? (default Neon Green):'
optional_string = string_input('What\'s the best colour ever?', 'Neon Green')

# prints 'Are you an admin (y/n):'
mandatory_boolean = boolean_input('Are you an admin?')

# prints 'Do you like python? (y/n default y):'
optional_boolean = boolean_input('Do you like python?', 'y')

# prints:
# red
# green
# blue
# Pick a colour:
mandatory_options = options_input('Pick a colour', ['red','green','blue'])

# prints:
# red
# green
# blue
# Pick a colour (default red):
optional_options = options_input('Pick a colour', 'red','green','blue'], 'red')
```

#### worklist
Pass a string to worklist describing what your code just did.

When the current `reactjo <cmd>` finishes running, reactjo core prints a friendly list of everything that just happened.

```
from helpers.worklist import worklist as wl
# Do something awesome
...

wl('Did something really cool!')
```
