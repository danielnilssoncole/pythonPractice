def square_numbers(nums):
    for i in nums:
        yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])
# my_nums = [i*i for i in [1,2,3,4,5]] #list comprehension
my_nums = (i*i for i in [1,2,3,4,5]) #generator comprehension

# print (my_nums)

# for num in my_nums:
#     print num


#convert generator to list
print list(my_nums)
