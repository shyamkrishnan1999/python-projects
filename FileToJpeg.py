
# Code to convert a given file to jpeg format

import os,sys
from PIL import Image


for infile in sys.argv[1:]:
    f, e=os.path.splitext(infile)
    outfile = f+".jpg"

    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("please Enter the correct path", infile)

