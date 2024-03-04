class Solution:
    def trap(self, height: List[int]) -> int:

        # stack=[]
        # ans=0
        # decre_next=0
        # for i,num in enumerate(height):
        #     while stack and num>=stack[-1][0]:
        #         element=stack.pop()
        #         popped,idx=element[0],element[1]
        #         space=popped * (i-idx-1)
        #         water=space-decre_next
        #         ans+=water
        #         decre_next+=(popped+water)
        #     if not stack:
        #         decre_next=0
        #     stack.append((num,i))

        # return ans

        max_prefix=[]
        max_suf=[]
        cur_max=height[0]
        for i,num in enumerate(height):
            cur_max=max(cur_max,num)
            max_prefix.append(cur_max)
        cur_max=height[-1]
        for i in range(len(height)-1,-1,-1):
            cur_max=max(cur_max,height[i])
            max_suf.append(cur_max)
        ans=0
        max_suf.reverse()
        for i,he in enumerate(height):
            ans+=min(max_suf[i],max_prefix[i])-he
        return ans      