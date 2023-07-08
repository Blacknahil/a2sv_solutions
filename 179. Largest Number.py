class wrapper:
    def __init__(self,val):
        self.val=str(val)
    def __lt__(self,other):
        return int(self.val+other.val)<int(other.val +self.val)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[wrapper(n) for n in nums]
        nums.sort(reverse=True)
        nums=[n.val for n in nums]
        return str(int(''.join(nums)))
