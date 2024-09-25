class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pstack=[]
        prefix=[]
        # prefix calculation
        for i,num in enumerate(arr):
            while pstack and pstack[-1][0]>=num:
                pstack.pop()
            if pstack:
                prefix.append(i-pstack[-1][1])
            else:
                prefix.append(i+1)
            pstack.append((num,i))
        suf_stack=[]
        suffix=[]
        # suffix calculation
        for i in range(len(arr)-1,-1,-1):
            while suf_stack and suf_stack[-1][0]>arr[i]:
                suf_stack.pop()
            if suf_stack:
                suffix.append((suf_stack[-1][1]-i))
            else:
                # if nothing on the stack it spans till the end
                suffix.append((len(arr)-i))
            suf_stack.append((arr[i],i))
        suffix.reverse()
        ans=0
        for i,num in enumerate(arr):
            ans+=((num)*(prefix[i] * suffix[i]))
        return ans%((10)**9+ 7)

        