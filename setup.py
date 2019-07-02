import sys

if 'install' in sys.argv:
    from os import system
    system('sudo cp crtlC ctrlP /usr/bin -v')

    print('clipboard was installed!!')
