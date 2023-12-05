class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        new_s=list(s)
        for i in range(len(s)):
            new_s[indices[i]]=s[i]
        return "".join(new_s)