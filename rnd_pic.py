#!/usr/bin/env python

from os import walk, system
import magic
import random
import subprocess 

def random_pic(pictures, ms):
    pic=''
    while True:
        pic = random.choice(pictures)
        if "image" in ms.file(pic):
            break
    return pic

def first_run():
    cmd = "/bin/pidof fvwm2"
    pid =  subprocess.Popen(
        cmd, 
        shell=True, 
        stdout=subprocess.PIPE
    ).stdout.read().strip()
    print "pid -> " ,pid
    with file('/home/jtimon/.fvwm/my_pid') as f:
        my_pid = f.read().strip()
    print "my_pid -> " ,my_pid

    if my_pid == pid:
        print "I am the same as my parent"
    else:
        print "first run"
        with file('/home/jtimon/.fvwm/my_pid', "w") as f:
            print >>f, pid



def main():
    mypath="/usr/share/backgrounds"
    mymagic = magic.open(magic.MAGIC_MIME_TYPE)
    mymagic.load()
    a=[]
    for (dirpath, dirnames, files) in walk(mypath):
        for filename in files:
            pic = '/'.join([dirpath, filename])
            print(pic)
            if 'image' in mymagic.file(pic):
                a.append(pic)

    cmd = "/usr/bin/Esetroot -scale {}".format(random.choice(a))
    print(a)
    system(cmd)

if __name__=="__main__":
    main()

