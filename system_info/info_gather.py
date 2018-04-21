#!/usr/bin/python3
import os, os.path
import sys
import shutil
import fnmatch
import subprocess
from pathlib import Path
import datetime

home=os.environ['HOME']
today=datetime.date.today()
today=today.strftime('%y%m%d')

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

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def mov_files(path,dfolder,value):

    # Create destination folder if it doesn't exist.
    ensure_dir(dpath)

    try:
        matches = get_files(path,value)
        for i in range(len(matches)):
            shutil.move(os.path.join(path,matches[i]),os.path.join(dpath,matches[i]))

def makdir(path):
    path=str(path)
    val=os.path.exists(path)
    if not val:
        com=['mkdir '+path]
        run_script(com)

def init():
    chk=Path(str(home)+"/archive")
    chk=str(chk)
    val=os.path.exists(chk)
    if not val:
        com=['mkdir '+chk]
        run_script(com)


def logging(step):
    archpath=Path(home+"/archive/")
    statusfile=Path(home+"/status."+today+".txt")
    if step == '0':
        if os.path.exists(str(statusfile)):
            darchpath=Path(str(archpath)+"/"+today+"/")
            darchpath=str(darchpath)
            makdir(darchpath)
            archcount=len([fn for fn in os.listdir(darchpath)])
            archcount=str(archcount)
            com=['mv $HOME/status.`date +%y%m%d`.txt $HOME/archive/`date +%y%m%d`/status_'+archcount+'.`date +%y%m%d`.txt']
            run_script(com)

        com = ['echo "Begin Status" > $HOME/status.`date +%y%m%d`.txt']
        run_script(com)
        com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
        run_script(com)
        com = ['echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" >> $HOME/status.`date +%y%m%d`.txt']
        run_script(com)
    elif step == '1':
        com = ['echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" >> $HOME/status.`date +%y%m%d`.txt']
        run_script(com)
        com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
        run_script(com)
        com = ['echo "End Status" >> $HOME/status.`date +%y%m%d`.txt']
        run_script(com)
    else:
        com = ['echo "Something went wrong!  Danger! Danger! Danger!" >> $HOME/status.`date +%y%m%d`.txt']
        run_script(com)

def drive():
    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo "Start of Phase 1: Storage Usage: " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)

    ofile = os.path.join(home,'status.' + today + '.txt')
    cmd = ['df', '-h']

    with open(ofile, "a") as outfile:
        subprocess.call(cmd , stdout=outfile)

    #com = ['df -h >> $HOME/status.`date +%y%m%d`.txt']
    #run_script(com)
    com = ['echo "End of Phase 1: Storage Usage: " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    
def ino():
    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo "Start of Phase 2: Inode Usage: " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)

    ofile = os.path.join(home,'status.' + today + '.txt')
    cmd = ['df', '-i']

    with open(ofile, "a") as outfile:
        subprocess.call(cmd , stdout=outfile)

    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo "End of Phase 2: Inode Usage: " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo " " >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)
    com = ['echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" >> $HOME/status.`date +%y%m%d`.txt']
    run_script(com)

def mainprocess():
    init()
    logging('0')
    drive()
    ino()
    logging('1')

def main():
    #Call the main menu
    mainprocess()

if __name__ == "__main__":
    sys.exit(main())
