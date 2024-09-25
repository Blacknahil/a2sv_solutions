class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans=[0 for _ in range(len(deck))]
        deck.sort()
        indexes=deque([i for i in range(len(deck))])
        for j in range(len(deck)):
            idx=indexes.popleft()
            ans[idx]=deck[j]
            if indexes:
                indexes.append(indexes.popleft())
        return ans
        