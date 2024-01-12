class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        right=k
        whites=blocks[left:right].count('W')
        min_whites=whites
        while right< len(blocks):
            if blocks[right]=="W":
                whites+=1
            if blocks[left]=="W":
                if whites !=0:
                     whites-=1
                else:
                     whites=0
            min_whites=min(min_whites,whites)
            right+=1
            left+=1
        return min_whites
