class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first_num=float("inf")
        second_num=float("inf")
        for num in nums:
            if num> second_num:
                return True
            if num > first_num:
                second_num=min(num,second_num)
            first_num=min(num,first_num)
        



        