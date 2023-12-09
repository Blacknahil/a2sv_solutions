class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        _min=float("inf")
        dic={_min:[]}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j] and _min>=i+j:
                    _min=i+j
                    if _min in dic:
                        dic[_min].append(list1[i])
                    else:
                        dic[_min]=[list1[i]]
        return dic[_min]


        