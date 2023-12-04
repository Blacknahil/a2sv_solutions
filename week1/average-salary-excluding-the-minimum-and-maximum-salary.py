class Solution:
    def average(self, salary: List[int]) -> float:
        lst_max=max(salary)
        lst_min=min(salary)
        total=0
        count=0
        for i in salary:
            if i!=lst_max and i!=lst_min:
                     total+=i
                     count+=1
        return total/count
