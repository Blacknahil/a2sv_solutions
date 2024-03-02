class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        visited=defaultdict(int)
        def nex(i):
            return (i+nums[i])%len(nums)

        for i in range(len(nums)):
            if visited[i]==1:
                continue
            slow,fast=i,nex(i)
            while nums[slow]*nums[fast]>0 and nums[slow]*nums[nex(fast)]>0:
                visited[slow]=1
                if slow==fast:
                    if slow!=nex(slow):
                        return True
                    break
                slow=nex(slow)
                fast=nex(nex(fast))
        return False


        
        