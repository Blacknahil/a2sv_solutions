class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        collection=set(fronts + backs)
        for i in range(len(fronts)):
            if backs[i] == fronts[i] and fronts[i] in collection:
                collection.remove(fronts[i])
        if collection:
            return min(collection)
        return 0

        