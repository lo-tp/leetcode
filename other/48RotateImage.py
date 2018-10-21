def finePrint(data):
    for i in xrange(0, len(data)):
        print data[i]

def swap(data, x,y):
    if data[x[0]][x[1]]!=data[y[0]][y[1]]:
        data[x[0]][x[1]]=data[x[0]][x[1]]^data[y[0]][y[1]]
        data[y[0]][y[1]]=data[x[0]][x[1]]^data[y[0]][y[1]]
        data[x[0]][x[1]]=data[x[0]][x[1]]^data[y[0]][y[1]]
def coordinatesCalculator(ini, length):
    length-=1
    ret=[ini]
    for i in xrange(0,3):
        ret.append([ret[i][1], length-ret[i][0]])
    return ret

class Solution(object):
    def rotate(self, matrix):
        length=len(matrix)
        size=length
        hCoor=0
        while length>1:
            for vCoor in xrange(hCoor,hCoor+length-1):
                coordinates=coordinatesCalculator([vCoor,hCoor], size)
                swap(matrix, coordinates[0], coordinates[1])
                swap(matrix, coordinates[0], coordinates[2])
                swap(matrix, coordinates[0], coordinates[3])
                # finePrint (matrix)
            length-=2
            hCoor+=1
