#python object oriented programming


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Daniel', 'Last', 50000)
emp2 = Employee('Test', 'User', 60000)


print emp1.fullname()
print Employee.fullname(emp1)
