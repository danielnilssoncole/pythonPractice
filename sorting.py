li = [9,1,8,2,7,3,6,4,5]

# s_li = sorted(li)
s_li = sorted(li, reverse=True)
# print('Sorted Variable: \t', s_li)

#.sort() only works on lists
# li.sort()
li.sort(reverse=True)
# print('Original Variable: \t', li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup) #sorted returns a list
# print 'Tuple:\t', s_tup

di = {'name': 'Daniel', 'job': 'programming', 'age': None, 'os': 'mac'}
s_di = sorted(di) #with dictionary, sorted returns list of sorted keys
# print 'Dict:\t', s_di

#sort ints based on absolute value
li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
# print s_li

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    # return emp.name
    # return emp.age
    return emp.salary

# s_employees = sorted(employees, key=e_sort) #key parameter takes in a function, built in or custom
s_employees = sorted(employees, key=e_sort, reverse=True)

from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('age'))
print s_employees
