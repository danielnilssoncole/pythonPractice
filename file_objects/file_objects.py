# file objects

#context manager - automatically closes file after block runs
#with open('test.txt', 'r') as f:
    # print every line
    # for line in f:
    #     print(line, end='')

    #list of lines
    #f_contents = f.readlines()

    # first n characters of file
    #f_contents = f.read(100)
    #print(f_contents)

    #f.tell()
    #f.seek()

#write ti files
# with open('test2.txt', 'w') as f:  #creates file if it does not exist. overwrites file if it does exist. use 'a' to append
#     f.write('*test*')

#copy file to new file
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

#images - binary mode
with open('earth.jpg', 'rb') as rf:
    with open('earth_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        wf.write(rf_chunk)
        # while len(rf_chunk) > 0:
        #     wf.write(rf_chunk)
        #     rf_chunk = rf.read(rf_chunk)
