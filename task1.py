#This is task1

f = open('Street_Centrelines.csv', 'r')

'''Tuple for names'''
def tuple_name():
    for line in file:
        line = line.split(',')
        name = (line[2], line[4], line[6], line[7])
        print(name)



