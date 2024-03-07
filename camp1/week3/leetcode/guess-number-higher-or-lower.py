# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def dp(left,right):
            middle=(left+right)//2
            b=guess(middle)
            l=guess(left)
            r=guess(right)
            if not b :
                return middle
            if not l:
                return left
            if not r:
                return right
            elif b==1:
                return dp(middle,right)
            else:
                return dp(left,middle)
        return dp(1,n)
        
        