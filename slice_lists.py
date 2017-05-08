my_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

#list[start:end:step]
# print my_list[::-1]

sample_url = 'http://github.com'
print sample_url

#reverse
print sample_url[::-1]

#get top level domain .com
print sample_url[-4:]

#print url without http://
print sample_url[7:]

#print without http:// or top level domain
print sample_url[7:-4]
