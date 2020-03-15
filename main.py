import exceptions
import subprocess
import json
import os
import sys
from time import sleep

argv = sys.argv
debug = False		          # Enable debug by default? (no)

with open('conf.json') as target:
	conf = json.load(target)

proc = conf['process']        # Process name
sl = conf['delay']            # Delay before next check

# Help text
help_txt = '''
Args:
Help: -h OR --help
Debug Mode: --debug
Specify a different process: main.exe example.exe

(c) Copyright 2020 ggpabuk
'''

# Working with startup arguments
for i in argv:
	if i == '--debug':
		debug = True
	elif i == '-h' or i == '--help':
		print(help_txt)
		sys.exit()
	else:
		proc = i

# Generate first signature
try:
	sign = subprocess.check_output(f'listdlls.exe {proc}')
except FileNotFoundError:
	exceptions.listdlls()
	sign = subprocess.check_output(f'listdlls.exe {proc}')

# Main Anti-Cheat code
while True:
	sign_new = subprocess.check_output(f'listdlls.exe {proc}')
	if sign_new != sign:
		os.system(f'taskkill /f /im {proc}')
		break
	elif sign_new != sign and debug:
		os.system(f'taskkill /f /im {proc}')
		print('Signatures not match')
		break
	elif sign_new == sign and debug:
		print('Signatures match')

	sleep(sl)

sys.exit()
