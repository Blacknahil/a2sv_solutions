class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard=["qwertyuiop","asdfghjkl","zxcvbnm"]
        dic={}
        ans=[]
        for i in range(3):
            for char in keyboard[i]:
                dic[char]=i
        for word in words:
            check_word=word.lower()
            expected=dic[check_word[0]]
            flag=True
            for char in check_word[1:]:
                if dic[char] != expected:
                    flag=False
                    break
            if flag:
                ans.append(word)
        return ans
                

        