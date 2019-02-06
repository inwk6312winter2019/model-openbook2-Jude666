#This is task1

f = open('Street_Centrelines.csv', 'r')
f = readline()
'''Tuple for names'''
def tuple_name():
    for line in f:
        line = line.split(',')
        name = (line[2], line[4], line[6], line[7])
        print(name)

'''Histogram for maintenance'''
def histogram():
    d = dict()
    for line in f:
        line = line.split(',')
        c = (line[12])
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    print(d)

'''List of unique owners for the streets'''
def owner_list():
    ownerList = []
    for line in f:
        line = line.split(',')
        i = line[11]
        if i not in ownerList:
            ownerList.append(i)
    print(ownerList)

'''Different types of street classes and list'''




