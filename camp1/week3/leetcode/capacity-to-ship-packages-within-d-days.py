class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(val):
            days_count=1
            cur_sum=0
            for weight in weights:
                cur_sum+=weight
                if cur_sum>val:
                    cur_sum=weight
                    days_count+=1
            return days_count<=days

        low=max(weights)
        high=sum(weights)

        while low<=high:
            mid=low+(high-low)//2
            if check(mid):
                high=mid-1
            else:
                low=mid+1
        return low