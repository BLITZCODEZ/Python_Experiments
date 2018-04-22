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
ofile=os.path.join(home,'status.' + today + '.txt')
archive=os.path.join(home,'archive/')

def wrifile(filename,value,wrtype,action):
    if wrtype == 0:
        with open(filename, "w") as outfile:
            if action == '0':
                act=writeln(value)
            elif action == '1':
                subprocess.call(cmd , stdout=outfile)
    elif wrtype == 1:
        with open(filename, "a") as outfile:
            if action == '0':
                act=writeln(value)
            elif action == '1':
                subprocess.call(cmd , stdout=outfile)

def get_files(path,value):
    matches = []
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files,value):
            matches.append(filename)
    # Sort files alphabetically
    matches.sort()

    return matches

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def mov_files(path,dfolder,value):

    # Create destination folder if it doesn't exist.
    ensure_dir(dfolder)

    matches = get_files(path,value)
    for i in range(len(matches)):
        shutil.move(os.path.join(path,matches[i]),os.path.join(dfolder,matches[i]))

def logging(step):
    if step == '0':
        filechk=get_files(home,"status.*.txt")
        filechkc=len(filechk)
        if filechkc > 0:
            darchpath=Path(archive+"/"+today)
            darchpath=str(darchpath)
            ensure_dir(darchpath)
            mov_files(home,archive+"/"+today,"status.*.txt")

        wrifile(ofile,"Begin Status",0,0)
        wrifile(ofile," ",1,0)
        wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",1,0)
    elif step == '1':
        wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",1,0)
        wrifile(ofile," ",1,0)
        wrifile(ofile,"End Status",1,0)
    else:
        wrifile(ofile,"Something went wrong!  Danger! Danger! Danger!",1,0)

def drive():
    wrifile(ofile," ",1,0)
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",1,0)
    wrifile(ofile,"Start of Phase 1: Storage Usage: ",1,0)
    wrifile(ofile," ",1,0)
    wrifile(ofile,"df -h",1,1)
    wrifile(ofile,"End of Phase 1: Storage Usage: ",1,0)
    wrifile(ofile," ",1,0)
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",1,0)
    wrifile(ofile," ",1,0)

def ino():
    wrifile(ofile," ",1,0)
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",1,0)
    wrifile(ofile,"Start of Phase 2: Inode Usage: ",1,0)
    wrifile(ofile," ",1,0)
    wrifile(ofile,"df -i",1,1)
    wrifile(ofile," ",1,0)
    wrifile(ofile,"End of Phase 2: Inode Usage: ",1,0)
    wrifile(ofile," ",1,0)
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",1,0)

def mainprocess():
    logging('0')
    drive()
    ino()
    logging('1')

def main():
    #Call the main menu
    mainprocess()

if __name__ == "__main__":
    sys.exit(main())
