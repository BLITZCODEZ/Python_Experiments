#!/usr/bin/python3
import os, os.path
import sys
import shutil
import fnmatch
import subprocess
from pathlib import Path
import datetime
import glob

home=os.environ['HOME']
today=datetime.date.today()
today=today.strftime('%y%m%d')
ofile=os.path.join(home,'status.' + today + '.txt')
archive=os.path.join(home,'archive/')
wt="war"

def wrifile(filename,value,wrtype,action):
    with open(filename, wt[wrtype]) as outfile:
            if action == 0:
                outfile.writelines(value)
            elif action == 1:
                subprocess.call(value , stdout=outfile)


def get_files(path,value):
    matches = []
    os.chdir(path)
    for filename in glob.glob(value):
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
            shutil.move(os.path.join(pals -lartth,matches[i]),os.path.join(dfolder,matches[i]))


def logging(step):
    if step == '0':
        filechk=get_files(home,"status.*.txt")
        filechkc=len(filechk)
        if filechkc > 0:
            print(filechk)
            print(filechkc)
            darchpath=Path(archive+"/"+today)
            darchpath=str(darchpath)
            ensure_dir(darchpath)
        try:
            mov_files(home,archive+today,"status.*.txt")
        except:
            print('home: '+home+' archive: '+archive+' filechk: '+str(filechk))

        wrifile(ofile,"Begin Status\n\n",0,0)
        wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",1,0)
    elif step == '1':
        wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",1,0)
        wrifile(ofile,"End Status\n",1,0)
    else:
        wrifile(ofile,"Something went wrong!  Danger! Danger! Danger!\n\n",1,0)

def drive():
    wrifile(ofile,"Start of Phase 1: Storage Usage: \n\n",1,0)
    wrifile(ofile,['df','-h'],1,1)
    wrifile(ofile,"\nEnd of Phase 1: Storage Usage.\n\n",1,0)
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",1,0)

def ino():
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",1,0)
    wrifile(ofile,"Start of Phase 2: Inode Usage: \n\n",1,0)
    wrifile(ofile,['df','-i'],1,1)
    wrifile(ofile,"\nEnd of Phase 2: Inode Usage.\n\n",1,0)
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
