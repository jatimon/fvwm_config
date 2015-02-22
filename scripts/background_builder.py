#!/usr/bin/env python

from __future__ import print_function
from os import walk, system
import magic
from collections import namedtuple

def main():
    mypath="/usr/share/backgrounds"
    a=[]
    Image=namedtuple('Image', ['name', 'path', 'fqp'])
    for (dirpath, dirnames, files) in walk(mypath):
        a+=[ Image(path=dirpath, name=file, fqp=dirpath+'/'+file) for file in files if "jpg" in file]

    mymagic = magic.open(magic.MAGIC_MIME_TYPE)
    mymagic.load()
    
    f=open('/home/jtimon/.fvwm/WallpaperMenu','w')
    for image in a:
        if "image" in mymagic.file(image.fqp):
            cmd="convert {0.fqp} -thumbnail 50x50 $HOME/.fvwm/temp_dir/{0.name}.png".format(image)
            system(cmd)
            menu="AddToMenu BackgroundMenu \"{0.name}\"%/home/jtimon/.fvwm/temp_dir/{0.name}.png% Function SetDefaultBackground {0.fqp}".format(image)
            print(menu, file=f)
    f.close()

if __name__=="__main__":
    main()
