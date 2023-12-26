class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for n, h in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]

        #one liner 

        