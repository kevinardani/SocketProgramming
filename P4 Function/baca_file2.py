f = open ('myfile.txt', 'r')

for line in f:
    print (line, end = '')
f.close()
