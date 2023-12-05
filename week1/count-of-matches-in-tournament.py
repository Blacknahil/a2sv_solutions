class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        tournaments=0
        while n>1:
            if n%2==0:
                n=n//2
                tournaments+=n
            else:
                tournaments+=n//2
                n= n//2 + 1
        return tournaments

        