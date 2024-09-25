class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=defaultdict(int)
        for others in answers:
            dic[others]+=1
        total=0
        for key in dic:
            if key + 1>=dic[key]:
                total+=key+1
            else:
               while dic[key]>0:
                   total+=key+1
                   dic[key]-=(key+1)
        return total
        