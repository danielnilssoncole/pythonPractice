import os

os.chdir('/Users/danielnilsson-cole/Desktop/projects/pythonPractice/rename_files/test_files')

for f in os.listdir(os.getcwd()):
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}-{}{}'.format(f_num, f_title, f_course, f_ext)

    os.rename(f, new_name)
