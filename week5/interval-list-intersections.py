class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1=0
        l2=0
        ans=[]
        while l2 < len(secondList) and l1 <len(firstList):
            interval=[max(firstList[l1][0],secondList[l2][0]),min(firstList[l1][1],secondList[l2][1])]
            if firstList[l1][1] > secondList[l2][1]:
                l2+=1
            else:
                l1+=1

            if interval[0]<=interval[1]:
                ans.append(interval)
        return ans


            