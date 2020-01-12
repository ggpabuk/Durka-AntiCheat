import os
import time
import subprocess
import psutil

proc_name = "GeometryDash.exe" # Имя процесса
sl = time.sleep

while True:
	for proc in psutil.process_iter():
	    name = proc.name()
	    # print(name)
	    if name == proc_name:
	    	with open(os.devnull, 'w') as f:
	    		subprocess.Popen('acB.exe', shell=True, stdout=f)
	sl(300)
