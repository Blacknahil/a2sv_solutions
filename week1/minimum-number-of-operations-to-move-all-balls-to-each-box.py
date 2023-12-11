class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        forward=[]
        backward=[]
        balls_left=0
        steps=0
        for box in boxes:
            steps+=balls_left
            forward.append(steps)
            if box=="1":
                balls_left+=1
        steps=0
        balls_right=0
        for i in range(len(boxes)-1,-1,-1):
            steps+=balls_right
            backward.append(steps)
            if boxes[i]=="1":
                balls_right+=1
        backward.reverse()
        for i in range(len(forward)):
            forward[i]=forward[i] + backward[i]
        return forward

        

        