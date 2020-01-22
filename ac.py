import subprocess
import time
import os
import sys

arg = sys.argv
debug = False

# Настройки
proc = "GeometryDash.exe" # Имя процесса
sleep = 5 # Задержка перед следующей проверкой
help_txt = "Агрументы:\nПомощь: -h или --help\nРежим отладки: --debug"

# Анти чит
def main():
	try:
		if arg[1] == "--debug":
			debug = True
		elif arg[1] == "-h" or arg[1] == "--help":
			print(help_txt)
			sys.exit()
	except IndexError:
		print("Запуск без агрументов!")

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
