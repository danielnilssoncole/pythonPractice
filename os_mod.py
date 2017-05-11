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

#os.walk returns dirpath dirnames and filenames for each dir
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print 'Current Path: ', dirpath
#     print 'Directories: ', dirnames
#     print 'Files: ', filenames
#     print 's'

#environment variables
# print os.environ.get('HOME')

#os.path.join - joins two paths
file_path = os.path.join(os.environ.get('HOME'), 'demo2.txt')
# print file_path

#os.path.basename - returns file name of path
# print os.path.basename('/tmp/test.txt')

#os.path.dirname - returns name of directory
# print os.path.dirname('/tmp/test.txt')

#os.path.split - returns tuple of dirname and basename
# print os.path.split('/tmp/test.txt')

#os.path.exists - checks if path exists
# print os.path.exists('/tmp/test.txt')

#os.path.isdir os.path.isfile - returns true or false if isfile or isdir

#os.path.splitext - returns tuple of path root and file extension
# print os.path.splitext('/tmp/test.txt')
