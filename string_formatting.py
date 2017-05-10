
person = {'name': 'Louis', 'age': 23}

#not good
# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print sentence

sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print sentence

sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print sentence

tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print sentence

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
# print sentence

l = ['Louis', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
# print sentence

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Elijah', '34')
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print sentence

sentence = 'My name is {name} and I am {age} years old.'.format(name='Elijah', age=34)
# print sentence

sentence = 'My name is {name} and I am {age} years old.'.format(**person) #unpack dictionary
# print sentence

#formatting digits {:02}
for i in range(1,11):
    sentence = 'The value is {:02}'.format(i)
    # print sentence

#decimal places {:.2f}
pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
# print sentence

#large number comma separators
# sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print sentence

#formatting date time
import datetime
my_date = datetime.datetime(1934, 7, 4, 12, 0, 0)
# print my_date
# print '{:%B %d, %Y}'.format(my_date) #March 1, 2000

#March 1, 2000 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(my_date)
print sentence
