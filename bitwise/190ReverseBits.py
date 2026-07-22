class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = [2**i for i in xrange(0, 32)]
        res = 0
        for i in xrange(0, 32):
            if n & bits[i]:
                res ^= bits[31-i]
        if res & bits[-1]:
            return -(2**32-res)
        return res

    def reverseBits(self, n: int) -> int:
        res = 0
        
        # We know we are strictly dealing with 32-bit integers
        for _ in range(32):
            # 1. Shift res to the left by 1 to make room for the incoming bit
            res <<= 1
            
            # 2. Extract the right-most bit from 'n' and add it to 'res'
            # (n & 1) isolates the last bit (0 or 1). 
            # The bitwise OR (|) adds it safely to res.
            res |= (n & 1)
            
            # 3. Shift 'n' to the right by 1 to process the next bit on the next iteration
            n >>= 1
            
        return res
