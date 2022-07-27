#!/bin/python3

import shutil    # For CopyFile
import os        # For GetFileSize and Check If File Exist
import sys       # For CLI Arguments


if(len(sys.argv) < 4):
    print("Missing arguments! Usage is script.py 10 5")
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])


if(os.path.isfile(file_name) == True):         # Check if MAIN logfile exist
    logfile_size = os.stat(file_name).st_size  # Get Filesize in BYTES
    logfile_size /= 1024                       # Convert from BYTES to KILOBYTES

    if(logfile_size >= limit_size):
        if(logs_number > 0):
            for current_file_num in range(logs_number, 1, -1):
                src = file_name + "_" + str(current_file_num-1)
                dst = file_name + "_" + str(current_file_num)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + " to " + file_name + "_1")
        my_file = open(file_name, 'w')
        my_file.close()
