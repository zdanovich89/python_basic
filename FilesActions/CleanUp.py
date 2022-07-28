import os
import time
from turtle import home

DAYS = 0.0000001     # Maximal age of file to stay, older will be deleted
FOLDERS = [
    '/home/yauhen/Documents/Trash_for_training/delete',
    '/home/yauhen/Documents/Trash_for_training/empty_folders',
    '/home/yauhen/Documents/Trash_for_training/trash'
]
TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0

now_time = time.time()                  # Get current time in SECONDS
age_time = now_time - 60*60*24*DAYS     # Period to deleting


def delete_old_files(folder):
    """Delete files older than x DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)  # Get full path to file
            modification_time = os.path.getmtime(file_name)
            if modification_time < age_time:
                size_file = os.path.getsize(file_name)
                TOTAL_DELETED_SIZE += size_file   # Count SUM of all free space
                TOTAL_DELETED_FILE += 1           # Count number of deleted files
                print("Deleting file: " + str(file_name))
                os.remove(file_name)


def delete_empty_folders(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            print("Deleting empty dir: " + str(path))
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_folders(folder)


# ===============MAIN===================

start_time = time.asctime()


for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_folders(folder)


finish_time = time.asctime()

print("-----------------------------------------")
print("Start time: " + str(start_time))
print("Total deleted size: " + str(int(TOTAL_DELETED_SIZE/1024/1024)) + "MB")
print("Total deletes files: " + str(TOTAL_DELETED_FILE))
print("Total deleted empty folders: " + str(TOTAL_DELETED_DIRS))
print("Finish time: " + str(finish_time))
print("-------------------EOF-------------------")
