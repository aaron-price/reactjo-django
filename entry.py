import sys, os, subprocess

from commands.new import new
from commands.scaffold import scaffold
from helpers.file_manager import file_manager as f

cmd = sys.argv[1]
if cmd in ['n', 'new']:
	new()
if cmd in ['b', 'build']:
	scaffold()
if cmd in ['s', 'server', 'serve']:
	os.chdir(f('$man', '$'))
	subprocess.Popen(['python', 'manage.py', 'runserver'])
