class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        right=k
        vowels=frozenset("aeiou")
        cur_vowels=0
        for char in s[left:right]:
            if char in vowels:
                cur_vowels+=1
        max_vowels=cur_vowels
        while right<len(s) and max_vowels !=k:
            if s[right] in vowels:
                cur_vowels+=1
            if s[left] in vowels:
                cur_vowels-=1
            left+=1
            right+=1
            max_vowels=max(max_vowels,cur_vowels)
        return max_vowels
        