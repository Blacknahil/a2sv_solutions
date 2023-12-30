class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[]
        def flips(right):
            left=0
            while left < right:
                arr[right],arr[left]=arr[left],arr[right]
                right-=1
                left+=1
        for i in range(n-1,-1,-1):
            _max=i
            for j in range(i):
                if arr[j] > arr[_max]:
                    _max=j
            if _max !=i:
                ans.append(_max+1)
                ans.append(i+1)
                flips(_max)
                flips(i)
        return ans
        



