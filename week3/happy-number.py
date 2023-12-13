class Solution:
    def isHappy(self, n: int) -> bool:
        visited=[]
        def cast_and_check(n):
            if n==1:
                return True
            else:
                if n in visited:
                    return False
                str_sum=0
                for i in str(n):
                    str_sum+=(int(i) **2)
                visited.append(n)
                return cast_and_check(str_sum)
        return cast_and_check(n)


        