class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        sz = len(num)
        if sz < 3:
            return False
        for length in range(1, 2 if num[0] == '0' else int((sz-1)/2)+1):
            a = int(num[:length])
            for length_2 in range(1, 2 if num[length] == '0' else int((sz-length)/2)+1):
                index = length+length_2
                b = int(num[length: index])
                while True:
                    if index == sz:
                        return True
                    c = a+b
                    if c and num[index] == '0':
                        break
                    c_str = str(c)
                    end_index = index+len(c_str)
                    if end_index <= sz and c_str == num[index:end_index]:
                        index, a, b = end_index, b, c
                    else:
                        break
        return False
