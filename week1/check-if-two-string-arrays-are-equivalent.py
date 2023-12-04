class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        concat1=""
        concat2=""
        for word in word1:
            concat1+=word
        for word in word2:
            concat2+=word
        return concat1==concat2
        