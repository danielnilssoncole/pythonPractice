#easier to ask forgiveness than permission (EAFP)
#look before you leap (LBYL)

#EAFP is better in most cases because:
#slightly faster where you don't expect a lot of exceptions
#checking multiple conditions means you have to access object multiple times 

#dictionaries
# person = {'name': 'J', 'age': 23, 'job': 'Programmer'}
person = {'name': 'J', 'age': 23}

#LBYL (non-pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print "I'm {name}. I'm {age} years old and I am a {job}".format(**person)
# else:
#     print 'Missing some keys'

#EAFP (pythonic)
# try:
#     print "I'm {name}. I'm {age} years old and I am a {job}".format(**person)
# except KeyError as e:
#     print "Missing {} key".format(e)


#lists
# my_list = [1,2,3,4,5,6]
my_list = [1,2,3,4,5]

#non-pythonic
# if len(my_list) >= 6:
#     print my_list[5]
# else:
#     print 'That index does not exist'

#pythonic
try:
    print my_list[5]
except IndexError:
    print 'That index does not exist'
