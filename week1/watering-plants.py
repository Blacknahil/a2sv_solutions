class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """ 
        steps=0
        cur_cap=capacity
        for i,water_needed in enumerate(plants):
            if cur_cap>=water_needed:
                steps+=1
                cur_cap-=water_needed
            else:
                steps=steps + (2*i ) + 1
                cur_cap=capacity
                cur_cap-=water_needed
        return steps

