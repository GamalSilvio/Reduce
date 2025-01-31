#Reduce uses a library in order to work, it is not a built in function
#Reduce is made up of two parts, the function and the sequence (data), and initial value (in this case 0)

from functools import reduce

my_list = [1,2,3]

def multiplyby2(item):
    return item*2

def onlyodd(item):
    return item %2 !=0

def accumulator(acc,item):
    return acc + item

print(reduce(accumulator, my_list, 0))
print(my_list)
