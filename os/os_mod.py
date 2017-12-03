import os
from datetime import datetime

# print(os.getcwd()) # get current directory
# print(os.listdir()) #list contents of directory
#os.chdir('/Users/danielnilsson-cole/Desktop/projects/') #change directory
#os.makedirs('new_folder/sub_folder') #makes new directory in directory
#os.rmdir('new_folder/sub_folder') #delete dir
# os.rename('new_folder', 'newFolder')
# os.stat('test.txt') #show info of file: size, modification time,
#ex: mod_time = os.stat('test.txt').st_mtime #modification time


#os.walk()
# for dirpath, dirnames, filenames in os.walk('/Users/danielnilsson-cole/Desktop/projects/pythonPractice/os/'):
#     print('current path: ', dirpath)
#     print('directories: ', dirnames)
#     print('files: ', filenames)
#     print()

def search_filename (path, query):
    matches = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if query in filename:
                matches.append({
                    'filename' : filename,
                    'parent_dir_path' : dirpath
                })
    if len(matches) > 0:
        print('\nFound {} file(s)\n'.format(len(matches)))
        for match in matches:
            print('- {0[filename]} - {0[parent_dir_path]}'.format(match))
        print()
    else:
        print('No files found')


search_filename(os.getcwd(), 'os')

# os.environ.get('HOME')

# os.path.join() Join one or more path components intelligently
#file_path = os.path.join(os.getcwd(), 'test2.txt')

# os.path.exists(os.getcwd())

#os.path.splitext(file_path)
