#file objects

# f = open('test.txt', 'r') # r, w, a, r+
#
# print f.name, f.mode
#
# f.close()

#context manager - # auto closes file
with open('test.txt', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readline()
    # f_contents = f.readlines()

    # for line in f:
    #     print line

    # f_contents = f.read(100) #returns next 100 characters of file

    size_to_read = 10
    # f_contents = f.read(size_to_read)

    # while len(f_contents) > 0:
    #     print f_contents, f.tell() #f.tell returns current position in file
    #     f_contents = f.read(size_to_read)

    f_contents = f.read(size_to_read)
    # print f_contents

    f.seek(0) #f.seek moves to specific position in files

    f_contents = f.read(size_to_read)
    # print f_contents

#writing to files
#if file does not exist, it will create it
#if it does exist, it will overwrite it
#use 'a' to append and not overwrite
# with open('test2.txt', 'w') as f:
#     f.write('Test')


#copy from one file to another
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)


#working with image files: rb, wb
#need to open images in binary mode: rb, wb
# with open('earth.jpg', 'rb') as rf:
#     with open('earth_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

with open('earth.jpg', 'rb') as rf:
    with open('earth_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
