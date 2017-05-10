import os
from datetime import datetime

#print current working directory
# print os.getcwd()

#change directory
# os.chdir('/Users/danielnilsson-cole/Desktop/projects/')

#list files and folders in working directory
# print os.listdir(os.getcwd())

#make new directory
#makedirs creates all intermediate directories for you, mkdir does not
# os.makedirs('os-demo/sub-dir-1')
# os.makedirs('os-demo-2')
# print os.listdir(os.getcwd())

#delete directories
#removedirs deletes all intermediate directories, rmdir does not
# os.removedirs('os-demo-2')
# print os.listdir(os.getcwd())

#rename folders and files
# os.rename('originalname', 'newname')
# os.rename('test.txt', 'demo.txt')
# print os.listdir(os.getcwd())

#print out info of files
# os.stat('name')
# print os.stat('demo.txt')
# print os.stat('demo.txt').st_size

#modified time
# modified_time = os.stat('demo.txt').st_mtime
# print datetime.fromtimestamp(modified_time)
