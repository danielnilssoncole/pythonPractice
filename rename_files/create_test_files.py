import os

# print os.getcwd()

# os.makedirs('test_files')
# print os.listdir(os.getcwd())

os.chdir('/Users/danielnilsson-cole/Desktop/projects/pythonPractice/rename_files/test_files')

planets = ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Pluto', 'Saturn', 'Sun', 'Uranus', 'Venus']
order_num = ['4', '6', '5', '2', '8', '10', '7', '1', '9', '3']
mod = 'Our Solar System'

for i in range(len(planets)):
    filename = '{0} - {1} - #{2}.txt'.format(planets[i], mod, order_num[i])
    with open(filename, 'w') as f:
        f.write(filename)
