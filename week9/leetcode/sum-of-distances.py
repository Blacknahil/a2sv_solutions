class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans=[0]*(len(nums))
        prefix={}
        n=len(nums)
        for i in range(n):
            if not nums[i] in prefix:
                prefix[nums[i]]=[0,i,1]
            else:
                dis,j,count=prefix[nums[i]]
                prefix[nums[i]][0]=dis+ (i-j)*count
                prefix[nums[i]][1]=i
                prefix[nums[i]][2]+=1
                ans[i]=prefix[nums[i]][0]
        nums.reverse()
        suffix={}
        for i in range(n):
            if not nums[i] in suffix:
                suffix[nums[i]]=[0,i,1]
            else:
                dis,j,count=suffix[nums[i]]
                suffix[nums[i]][0]=dis+(i-j)*count
                suffix[nums[i]][1]=i
                suffix[nums[i]][2]+=1
                ans[n-i-1]+=suffix[nums[i]][0]
        return ans

        