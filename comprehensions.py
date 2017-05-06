nums = [1,2,3,4,5,6,7,8,9,10]

#n for each n in nums
my_list = [n for n in nums]
# print my_list

#n*n for each n in nums
my_list = [n**2 for n in nums]
# print my_list

#n for each n in nums if n is even
my_list = [n for n in nums if n%2 == 0]
# print my_list

# (letter, num) pair for each letter in 'abcd' and each num in '0123'
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print my_list

#dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#zip(names, heros) zip produces list tuples: (name, hero)

#dict{'name': 'hero'} for each name,hero in zip(names,heros)
my_dict = {name: hero for name, hero in zip(names, heros)}
#if name is not Peter
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print my_dict

# set comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
my_set = {n for n in nums}
# print my_set
