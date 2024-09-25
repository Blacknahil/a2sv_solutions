class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        if total%p==0:
            return 0
        if total<p:
            return -1
        prefix=[0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        reminder=total%p
        dic={0:0}
        shortest=len(nums)
        for right in range(1,len(prefix)):
            r=prefix[right]%p
            if (r-reminder)%p in dic:
                shortest=min(shortest,right-dic[(r-reminder)%p])
            dic[r]=right
        if shortest==len(nums):
            return -1
        return shortest


            

        