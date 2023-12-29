class Solution:
    def sortSentence(self, s: str) -> str:
        # is2 sentence4 This1 a3"
        #  This   is a sentence 
        # arr
        # arr.sort(key=lambda word:word[-1])
        arr=s.split(" ")
        arr.sort(key=lambda word: word[-1])
        ans=''
        for i in range(len(arr)):
            arr[i]=arr[i][:-1]
        return " ".join(arr)