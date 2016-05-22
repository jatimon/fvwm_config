#!/usr/bin/env python

from __future__ import print_function
import os
import magic

def main():
    mypath="/usr/share/backgrounds"
    mymagic = magic.open(magic.MAGIC_MIME_TYPE)
    mymagic.load()
    a = []
    for (dirpath, dirnames, files) in os.walk(mypath):
        for filename in files:
            pic = '/'.join([dirpath, filename])
            if 'image' in mymagic.file(pic):
                a.append(pic)                               

    
    home = os.environ['HOME']
    f = open('{}/.fvwm/WallpaperMenu'.format(home),'w')
    for image in a:
        basename = os.path.basename(image)
        if not os.path.isfile(
            "{}/.fvwm/temp_dir/{}.png".format(home, basename.split('.')[0])
        ):
            cmd = (
                    "convert {} -thumbnail 50x50 "
                    "$HOME/.fvwm/temp_dir/{}.png".format(
                        image,
                        basename.split('.')[0]
                    )
            ) 
            print(cmd)
            os.system(cmd)

        menu = (
              'AddToMenu BackgroundMenu "{}"'
              '"%/home/jtimon/.fvwm/temp_dir/{}.png%" '
              'Function SetDefaultBackground {}'.format(
                  basename,
                  basename.split('.')[0],
                  image
                ))
        print(menu, file=f)
    f.close()

if __name__ == "__main__":
    main()
