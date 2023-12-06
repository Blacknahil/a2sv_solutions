class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        list_s=[]
        max_word=0
        cur_word=""
        for i,char in enumerate(s):
            if char==" ":
                list_s.append(cur_word)
                max_word=max(max_word,len(cur_word))
                cur_word=""
            elif i==len(s)-1:
                cur_word+=char
                list_s.append(cur_word)
                max_word=max(max_word,len(cur_word))
            else:
                cur_word+=char
        ans=[]
        for i in range(max_word):
            cur=""
            for word in list_s:
                if i<len(word):
                    cur+=word[i]
                else:
                    cur+=" "
            cur=cur.rstrip(" ")
            ans.append(cur)
        return ans


        

        