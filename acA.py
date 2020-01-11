import os
import time
import subprocess
import psutil
from win32com.shell import shell, shellcon

sl = time.sleep
print(shell.SHGetFolderPath(0, shellcon.CSIDL_STARTUP, None, 0)) # Добавление файла в автозагрузку

while True:
	for proc in psutil.process_iter():
	    name = proc.name()
	    # print(name)
	    if name == "GeometryDash.exe":
	    	with open(os.devnull, 'w') as f:
	    		subprocess.Popen('ac.py', shell=True, stdout=f)
	sl(300)
