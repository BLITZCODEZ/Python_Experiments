#!/usr/bin/python3
import os
import sys
import shutil
import fnmatch
import subprocess

def user_input(msg):
	
	uinput = ''
	
	if sys.version_info[0] == 3:
		uinput = input(msg)
	else:
		uinput = raw_input(msg)
		
	uinput = str(uinput)
	
	return uinput

def pause():
	#Wait for input from the user.
	pausep = user_input("Press the <ENTER> key to continue...")
	
def run_script(value):
	
	com = None
	
	if sys.version_info[0] == 2:
		com = ''
		for ei in value:
			com += ei
			com += ' '
	else:
		com = value
		
	subprocess.call(com,shell=True)

def drive():
	com = ['df','-h']
	run_script(com)
	
def ino():
	com = ['df','-i']
	run_script(com)
	
def logs():
	print("Good Morning Dave.")
	
def mainmenu():
	
	while True:
		menu = {}
		menu[1] = "Space check"
		menu[2] = "Inode check"
		menu[3] = "Log check"
		ops=menu.keys()
		_=os.system("clear")
		print("Linux Sysadmin Report")
		print('')
		for entry in ops:
			opt = '%02d' % entry
			print (opt, menu[entry])
		print('')
		sel=user_input("Please Select: ")
		print (sel)
		if sel == '1':
			drive()
			pause()
		elif sel == '2':
			ino()
			pause()
		elif sel == '3':
			logs()
			pause()
		else:
			print("I can't let you do that Dave")
			pause()

def main(args):
    #Call the main menu
    mainmenu()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
