class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.dic={}
        self.life=timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId]=[currentTime,currentTime +self.life]
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dic and currentTime < self.dic[tokenId][1]:
            self.dic[tokenId][1]=currentTime + self.life
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for key in self.dic.keys():
            if self.dic[key][0] < currentTime < self.dic[key][1]:
                count+=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)