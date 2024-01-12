class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index={}
        min_len=float("inf")
        for i,card in enumerate(cards):
            if card in last_index:
                min_len=min(min_len,i-last_index[card] + 1)
            last_index[card]=i
        if min_len==float("inf"):
            return -1
        return min_len
        

        