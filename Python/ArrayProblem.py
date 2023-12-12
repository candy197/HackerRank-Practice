import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    reversed_arr = numpy.array(arr[::-1], float)
    return reversed_arr
    #one Line Answers
    #numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)