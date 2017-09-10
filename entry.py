from commands.new import new
from commands.scaffold import scaffold
import sys

cmd = sys.argv[1]
if cmd in ['n', 'new']:
	new()
if cmd in ['s', 'scaffold']:
	scaffold()
