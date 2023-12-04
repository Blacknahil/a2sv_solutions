class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans=[]
        _max=max(candies)
        for candy in candies:
            if candy + extraCandies >= _max:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        