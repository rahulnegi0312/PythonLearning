import os
import subprocess as sp
print('Hello world')
print('Rahul')
#command="python3 --version"
#os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
prog="Notepad.exe"
file="hello.txt"
sp.Popen([prog,file])