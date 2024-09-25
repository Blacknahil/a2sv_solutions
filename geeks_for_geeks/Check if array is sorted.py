#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        left,right=0,1
        while right<len(arr):
            if arr[left]>arr[right]:
                return False
            left+=1
            right+=1
    
        return True
