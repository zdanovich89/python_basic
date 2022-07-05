import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help Requested")
        print("Usage this program is: python myfile.py argv1 argv2")
    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Arguments NOT PROVIDED")

os.system("ls -la")
sys.exit()