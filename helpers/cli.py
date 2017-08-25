import os
import subprocess
from helpers.path_manager import path_manager as p

def npm(args):
	os.chdir(p('package.json'))
	subprocess.call(['npm'] + args)

def manage(args):
	os.chdir(p('backend_project'))
	subprocess.call(['python3', 'manage.py'] + args)

def pip(args):
	subprocess.call(['pip3'] + args)

def startproject(name):
	os.chdir(p('backend'))
	subprocess.call(['django-admin', 'startproject', name])

def startapp(name):
	os.chdir(p('backend_project'))
	subprocess.call(['python3', 'manage.py', 'startapp', name])
