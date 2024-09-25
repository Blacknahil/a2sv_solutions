class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visited={}
        def dp(left,right,turn):
            if left>right:
                return 0
            if (left,right,turn) in visited:
                return visited[(left,right,turn)]
            res=0
            if turn=="1":
                res=max(nums[right]+dp(left,right-1,"2"),nums[left]+ dp(left+1,right,"2"))
            if turn=="2":
                res=min(dp(left+1,right,"1"),dp(left,right-1,"1"))
            visited[(left,right,turn)]=res
            return res
        player1=dp(0,len(nums)-1,"1")
        return player1>=sum(nums)-player1
        
