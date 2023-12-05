class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """

        dic={"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i", "10#":"j", "11#":"k", "12#":"l" , "13#":"m" , "14#":"n", "15#":"o", "16#":"p", "17#":"q", "18#":"r", "19#":"s", "20#":"t", "21#":"u", "22#":"v", "23#":"w", "24#":"x", "25#":"y", "26#":"z"
        }
        ans=""
        right=len(s)-1
        while right>=0:
            if s[right]!="#":
                ans+=dic[s[right]]
                right-=1
            else:
                ans+=dic[s[right-2:right+1]]
                right-=3
        return ans[::-1]