#!/usr/bin/env python

from os import walk, system
import magic
import random

def random_pic(pictures, ms):
    pic=''
    while True:
        pic = random.choice(pictures)
        if "image" in ms.file(pic):
            break
    return pic

def main():
    mypath="/usr/share/backgrounds"
    a=[]
    for (dirpath, dirnames, files) in walk(mypath):
        a += [dirpath + "/" + file for file in files ]
    
    mymagic = magic.open(magic.MAGIC_MIME_TYPE)
    mymagic.load()
    
    system("/usr/bin/Esetroot -scale " +  random_pic(pictures=a, ms=mymagic) )

if __name__=="__main__":
    main()

