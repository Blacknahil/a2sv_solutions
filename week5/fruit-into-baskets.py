class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        _max=start=0
        count={}
        for i, fruit in enumerate(fruits):
            count[fruit]=count.get(fruit,0) + 1
            while len(count) > 2:
                count[fruits[start]]-=1
                if count[fruits[start]]==0:
                    del count[fruits[start]]
                start+=1
            _max=max(_max,i-start+1)
        return _max
           
                    

            