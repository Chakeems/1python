f = open('mytext.txt', 'r')

for line in f:
    print (line,end='') 

# firstline = f.readline()
# secondline=f.readline()
# thirdline = f.readline()
# fourthline = f.readline()
# fifthline = f.readline()
# print (firstline)
# print (secondline)
# print (thirdline)
# print(fourthline)
# print(fifthline)
f.close()