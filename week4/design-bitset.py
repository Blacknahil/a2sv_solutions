class Bitset:

    def __init__(self, size: int):
        self.zeros=set([i for i in range(size)])
        self.ones=set()


    def fix(self, idx: int) -> None:
        if idx in self.zeros:
            self.ones.add(idx)
            self.zeros.remove(idx)
        

    def unfix(self, idx: int) -> None:
        if idx in self.ones:
            self.zeros.add(idx)
            self.ones.remove(idx)
        
    def flip(self) -> None:
        self.zeros,self.ones=self.ones,self.zeros

    def all(self) -> bool:
        return len(self.zeros)==0
        

    def one(self) -> bool:
        return len(self.ones) !=0
        

    def count(self) -> int:
        return len(self.ones)
        

    def toString(self) -> str:
        st=["0"] * (len(self.ones) + len(self.zeros))
        for i in self.ones:
            st[i]="1"
        return "".join(st)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()