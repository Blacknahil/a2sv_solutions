class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic={}
        quarter=len(arr)//4
        for num in arr:
            dic[num]=dic.get(num,0) + 1
            if dic[num] >quarter:
                return num
