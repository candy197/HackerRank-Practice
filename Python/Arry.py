import numpy

if __name__ == "__main__":
    arr = list(map(int,(input().split())))

NArr = numpy.array(arr).reshape((3,3))
print(NArr)
try:
    print(NArr)
except Exception as e :
    print("Error: ", e)