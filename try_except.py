#else clause only runs if know exception is thrown
#finally runs always, if exceotions are thrown or if not

try:
    f = open('test.txt')
    #manually raise exception
    # if f.name == 'test.txt':
    #     raise Exception
except IOError as e:
    print e
except Exception as e:
    print 'Error!'
else:
    print f.read()
    f.close
# finally:
#     pass
