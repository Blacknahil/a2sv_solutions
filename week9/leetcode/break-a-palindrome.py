class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i]!="a" and i!=len(palindrome)//2:
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:len(palindrome)-1] + "b"