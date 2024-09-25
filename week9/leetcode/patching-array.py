class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        pt=0
        prefix=1
        patch=0
        while prefix<=n:
            if pt<len(nums) and prefix>=nums[pt]:
                prefix+=nums[pt]
                pt+=1
            else:
                patch+=1
                prefix+=prefix
        return patch

        