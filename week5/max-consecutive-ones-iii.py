class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest=0
        left=right=0
        while right < len(nums):
            if nums[right]==0:
                k-=1
            while k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            longest=max(longest,right-left+1)
            right+=1
        return longest
    # when zeros > k: we move the left pointer till we find a sub array with less than or equal to k : decrement l-1: when the left pointer gets an aray less than or equal to k exit loop and move the right pointer
    #when the right pointer gets to the last element stop the iteration after the left pointer gets the number of zeros to less than or equal to k