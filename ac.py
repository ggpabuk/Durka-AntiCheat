import subprocess
import time
import os
import sys

# Настройки
proc = "GeometryDash.exe" # Имя процесса
sleep = 5 # Задержка перед следующей проверкой
debug = False # Режим отладки

# Анти чит
def main():
	sign = subprocess.check_output('listdlls.exe ' + proc)
	while True:
		sign_new = subprocess.check_output('listdlls.exe ' + proc)
		if sign == sign_new:
			if debug == True:
				print("Сигнатуры совпали")
		else:
			if debug == True:
				print("Сигнатуры НЕ совпали")
			os.system("taskkill /f /im " + proc)
			sys.exit() # Завершение процесса AC
		time.sleep(sleep)

if __name__ == '__main__':
	main()
