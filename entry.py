"""Takes in the reactjo command and, if necessary, executes a command module"""
import sys

from commands.new import new
from commands.content import content
from commands.production import production

CMD = sys.argv[1]
if CMD in ['n', 'new']:
    new()
if CMD in ['c', 'content']:
    content()
if CMD in ['p', 'prod', 'production']:
    production()
