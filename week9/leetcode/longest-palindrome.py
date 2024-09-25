class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=defaultdict(int)
        longest=0
        for char in s:
            dic[char]+=1
        odd_taken=False
        for val in dic.values():
            #if the count is even
            if val%2==0:
                longest+=val
            #i can take one odd and make the length of
            # the result a odd but it should be only one 
            elif val%2 and not odd_taken:
                longest+=val
                odd_taken=True
            else:
                longest+=(val-1)
        return longest