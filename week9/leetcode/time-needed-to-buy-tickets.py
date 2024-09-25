class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        for i,ticket in enumerate(tickets):
            if ticket>tickets[k] and i<k:
                time+=tickets[k]
            elif ticket > tickets[k] and i>k:
                time+=tickets[k]-1
            elif ticket<tickets[k]:
                time+=ticket
            elif i>k:
                time+=tickets[k]-1
            else:
                time+=tickets[k]
        return time
        