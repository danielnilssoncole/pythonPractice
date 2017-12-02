import os
from datetime import datetime

print(os.getcwd()) # get current directory
#print(os.listdir()) #list contents of directory
#os.chdir('/Users/danielnilsson-cole/Desktop/projects/') #change directory
#os.makedirs('new_folder/sub_folder') #makes new directory in directory
#os.rmdir('new_folder/sub_folder') #delete dir
# os.rename('new_folder', 'newFolder')
# os.stat('test.txt') #show info of file: size, modification time,
#ex: mod_time = os.stat('test.txt').st_mtime #modification time


#os.walk()
for dirpath, dirnames, filenames in os.walk('/Users/danielnilsson-cole/Desktop/projects/pythonPractice/os/'):
    print('current path: ', dirpath)
    print('directories: ', dirnames)
    print('files: ', filenames)
    print()

def search_dir(path, query):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if query in filename:
                files.append({
                    'filename' : filename,
                    'parent_dir_path' : dirpath
                })
