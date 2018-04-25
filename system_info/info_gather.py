#!/usr/bin/python3
import os, os.path
import sys
import shutil
import fnmatch
import subprocess
from pathlib import Path
import time
import glob

home=os.environ['HOME']
today=time.strftime('%y%m%d-%H%M%S')
archday=time.strftime('%y%m%d')
ofile=str(os.path.join(home,'status.' + today + '.txt'))
archive=str(os.path.join(home,'archive/'+archday))
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
            shutil.move(os.path.join(path,matches[i]),os.path.join(dfolder,matches[i]))

def startlog():
    wrifile(ofile,"Begin Status\n\n",0,0)
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",1,0)

def endlog():
    wrifile(ofile,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",1,0)
    wrifile(ofile,"End Status\n",1,0)

def archfiles():
    ensure_dir(archive)
    mov_files(home,archive,"status.*.txt")

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
    archfiles()
    startlog()
    drive()
    ino()
    endlog()
    print(open(home+'/status.'+today+'.txt',wt[2]).read())

mainprocess()

#def main():
    ##Call the main menu
    #mainprocess()

#if __name__ == "__main__":
    #sys.exit(main())
