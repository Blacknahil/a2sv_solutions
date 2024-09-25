class Solution:
    def fib(self, n: int) -> int:
        visited={}
        def recurse(n,visited):
            if n==0:
                return 0
            if n==1:
                return 1
            if n in visited:
                return visited[n]
            first=recurse(n-1,visited)
            second=recurse(n-2,visited)
            visited[n]=first+second
            return first + second
        
        return recurse(n,visited)
        