class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic=dict()
        n_arr2=[]
        for i in arr1:
            if i in arr2:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
            else:
                n_arr2.append(i)
        n_arr2.sort()
        sorted_arr=[]
        for i in arr2:
            key=dic[i]
            sorted_arr+=[i]*key
        sorted_arr+=n_arr2
        return sorted_arr        
        

