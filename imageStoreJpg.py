#!/usr/bin/env python

import sys, os, subprocess
from PIL import Image

threshold = 0.8
SERVALDBINARY = "/usr/local/bin/servald"
max_size = 500 # Maximum horizontal or vertical resolution

im = Image.open(sys.argv[1])
im.thumbnail((max_size, max_size), Image.ANTIALIAS)
export_path = "/tmp/"+".".join(sys.argv[2].split(".")[0:-1])+"_resized.jpg"
im.save(export_path)

export_size = os.path.getsize(export_path)
original_size = os.path.getsize(sys.argv[1])

quota = float(export_size) / float(original_size)
sys.stderr.write("Quota: "+str(quota)+"\n")

if quota < threshold:
    sys.stderr.write("quota < threshold, inserting new image.\n")
    result = subprocess.check_output([SERVALDBINARY, "rhizome", "add", "file", sys.argv[5], export_path])
    print(result)
    os.remove(export_path)
    sys.exit(0)
    
else:
    os.remove(export_path)
    sys.exit(1)