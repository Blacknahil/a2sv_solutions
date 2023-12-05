class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        left=0
        right=2
        max_sub=[]
        while right<len(num):
            if len(set(list(num[left:right+1])))==1:
                    max_sub.append(num[left:right+1])
            right+=1
            left+=1
        max_sub.sort()
        if max_sub:
            return max_sub[-1]
        return ""
        