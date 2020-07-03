import easygui as eg
import sys
from pathlib import Path
from zipfile import ZipFile
import os.path
import os
import py7zr
import pyunpack

userpath = str(Path.home())
userpath = userpath + '\\AppData\\Local\\ACPythonScript\\'
try:
    os.mkdir(userpath)
except OSError:
    print("Creation of the directory %s failed" % userpath)
else:
    print("Successfully created the directory %s " % userpath)


def getgamepath():
    global modcars
    global modtracks
    global accars
    global actracks

    # Makes the txt files if they do not exist
    f = open(userpath + "acpath.txt", "a")
    f.close()
    f = open(userpath + "modpath.txt", "a")
    f.close()

    print("Reading txt files")

    # Reads the files for the paths
    acc = open(userpath + "acpath.txt", "r")
    ac = acc.read()
    acc.close()
    modread = open(userpath + "modpath.txt", "r")
    mod = modread.read()
    modread.close()

    print("Done...")

    try:
        os.mkdir(mod+'cars\\')
    except FileExistsError:
        pass
    try:
        os.mkdir(mod+'tracks\\')
    except FileExistsError:
        pass

    modcars = (mod+'cars\\')
    modtracks = (mod+'tracks\\')
    print(modtracks)
    accars = (ac+'cars\\')
    actracks = (ac+'tracks\\')
    print(actracks)


def extractcars():
    arr = os.listdir(modcars)
    try:
        firstfile = arr[0]
    except IndexError:
        return

    pathtozip = modcars+firstfile

    if firstfile.endswith('.7z'):
        archive = py7zr.SevenZipFile(pathtozip, mode='r')
        archive.extractall(path=accars)
        archive.close()
        if os.path.exists(path=pathtozip):
            os.remove(path=pathtozip)
        else:
            print("The file doesn't exist")
    elif firstfile.endswith('.zip'):
        zf = ZipFile(pathtozip, 'r')
        zf.extractall(accars)
        zf.close()
        if os.path.exists(path=pathtozip):
            os.remove(path=pathtozip)
        else:
            print("The file doesn't exist")
    elif firstfile.endswith('.rar'):
        pyunpack.Archive(pathtozip).extractall(accars)
        if os.path.exists(path=pathtozip):
            os.remove(path=pathtozip)
        else:
            print("The file doesn't exist")
    else:
        print("Extract Car Function Error")

def extracttracks():
    arr = os.listdir(modtracks)
    try:
        firstfile = arr[0]
    except IndexError:
        return

    pathtozip = modtracks+firstfile
    print(pathtozip)

    if firstfile.endswith('.7z'):
        archive = py7zr.SevenZipFile(pathtozip, mode='r')
        archive.extractall(path=modtracks)
        archive.close()
        if os.path.exists(path=pathtozip):
            os.remove(path=pathtozip)
        else:
            print("The file doesn't exist")
    elif firstfile.endswith('.zip'):
        zf = ZipFile(pathtozip, 'r')
        zf.extractall(modtracks)
        zf.close()
        if os.path.exists(path=pathtozip):
            os.remove(path=pathtozip)
        else:
            print("The file doesn't exist")
    elif firstfile.endswith('.rar'):
        pyunpack.Archive(pathtozip).extractall(actracks)
        if os.path.exists(path=pathtozip):
            os.remove(path=pathtozip)
        else:
            print("The file doesn't exist")
    elif firstfile.endswith('.crdownload'):
        return
    else:
        return


getgamepath()
while True:
    extractcars()
    extracttracks()