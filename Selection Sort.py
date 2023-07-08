class Solution: 
    def select(self, arr, start):
        n=len(arr)
        for i in range(n-start):
            min_index=i
            for j in range(i,n):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
        # code here 
    
    def selectionSort(self, arr,n):
        return self.select(arr,0)
