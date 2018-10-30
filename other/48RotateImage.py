def calculateCoordinators(original, length):
    data=[original]
    for i in xrange(0,3):
        data.append([data[i][1], length-data[i][0]])
    return data

class Solution(object):
    def rotate(self, matrix):
        length=len(matrix)-1
        operationNum=length
        startPos=0
        while operationNum>=1:
            for i in xrange(0, operationNum):
                cs=calculateCoordinators([startPos, startPos+i], length)
                matrix[cs[0][0]][cs[0][1]],matrix[cs[1][0]][cs[1][1]]=matrix[cs[1][0]][cs[1][1]],matrix[cs[0][0]][cs[0][1]]
                matrix[cs[0][0]][cs[0][1]],matrix[cs[3][0]][cs[3][1]]=matrix[cs[3][0]][cs[3][1]],matrix[cs[0][0]][cs[0][1]]
                matrix[cs[2][0]][cs[2][1]],matrix[cs[3][0]][cs[3][1]]=matrix[cs[3][0]][cs[3][1]],matrix[cs[2][0]][cs[2][1]]
            startPos+=1
            operationNum-=2
