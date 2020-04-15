from time import sleep

import requests
import subprocess
import yaml
import os

with open('config.yaml') as target:
	cfg = yaml.load(target, Loader=yaml.FullLoader)

# Take the variables from the configuration file
# To change these variables, edit "config.yaml"
process = cfg['process']
delay = cfg['delay']
debug = cfg['debug']

# Download listdlls if it was not found earlier
def get_listdlls():
	target = open('listdlls.exe', 'wb')
	ufr = requests.get('https://www.dropbox.com/s/by4ca7zwzcqyt12/Listdlls.exe')
	target.write(ufr.content)

	target.close()

# Generate first signature
try:
	signature = subprocess.check_output(f'listdlls.exe {process}')
except FileNotFoundError:
	get_listdlls()

	signature = subprocess.check_output(f'listdlls.exe {process}')

# Main Anti-Cheat code
while True:
	signature_new = subprocess.check_output(f'listdlls.exe {process}')
	if signature_new != signature:
		os.system(f'taskkill /f /im {process}')
		break
	elif signature_new != signature and debug:
		os.system(f'taskkill /f /im {process}')
		print('Signatures not match')
		break
	elif signature_new == signature and debug:
		print('Signatures match')

	sleep(delay)
