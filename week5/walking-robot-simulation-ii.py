class Robot:

    def __init__(self, width: int, height: int):
        self.dxn="East"
        self.pos=[0,0]
        self.height=height
        self.width=width
        self.moves=0

    def step(self, num: int) -> None:
        self.moves+=num
        while num>0:
            num=num%(2*self.height + 2*self.width -4)
            if self.dxn=="East":
                if self.pos[0] + num < self.width:
                    self.pos[0]+=num
                    num=0
                else:
                    num-=(self.width-self.pos[0]-1)
                    self.pos[0]=self.width-1
                    self.dxn="North"
                   
            elif self.dxn=="North":
                if self.pos[1] + num <self.height:
                    self.pos[1]+=num
                    num=0
                else:
                    num-=(self.height-self.pos[1]-1)
                    self.pos[1]=self.height-1
                    self.dxn="West"

            elif self.dxn=="West":
                if self.pos[0]-num >=0:
                    self.pos[0]-=num
                    num=0
                else:
                    num-=self.pos[0]
                    self.pos[0]=0
                    self.dxn="South"
            elif self.dxn=="South":
                if self.pos[1] - num>=0:
                    self.pos[1]-=num
                    num=0
                else:
                    num-=self.pos[1]
                    self.pos[1]=0
                    self.dxn="East"
        if self.pos==[0,0] and self.moves:
                self.dxn="South"          
                    
        #check the four dxn from east, then not one at a time 
        # east
        #NORTH
        #west
        #south
        

    def getPos(self) -> List[int]:
        return self.pos
        #cur
        

    def getDir(self) -> str:
        return self.dxn
        #dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()