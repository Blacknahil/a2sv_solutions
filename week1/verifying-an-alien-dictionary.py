class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def comparator(char1,char2,order):
            return order.index(char1) < order.index(char2)
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            pointer=0
            while pointer <min(len(word1),len(word2)) and word1[pointer] ==word2[pointer]:
                pointer+=1
            if pointer < min(len(word1),len(word2)):
                if not comparator(word1[pointer],word2[pointer],order):
                    return False
            else:
                if word1 > word2:
                    return False
        return True
            

        