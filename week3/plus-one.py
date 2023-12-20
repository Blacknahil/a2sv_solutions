class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''
        lst=[]
        for i in digits:
            i=str(i)
            num+=i
        num=int(num)+1
        num=str(num)
        for j in num: 
            j=int(j)
            lst+=[j]
        return lst

