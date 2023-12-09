class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        equal=[]
        greater=[]
        less=[]
        for num in nums:
            if num>pivot:
                greater.append(num)
            elif num<pivot:
                less.append(num)
            else:
                equal.append(num)
        return less+equal+greater