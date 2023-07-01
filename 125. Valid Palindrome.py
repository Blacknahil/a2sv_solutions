class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        new_str=""
        for char in s:
            if char.isalpha():
                new_str+=char.lower()
            elif char.isnumeric():
                new_str+=char
        return new_str==new_str[::-1]
