class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res=[0 for _ in range(len(nums))]
        indexes=[i for i in range(len(nums))]

        def merge(left_half,right_half):
            ans,p1,p2=[],0,0
            count=0
            while p1<len(left_half) and p2< len(right_half):

                if nums[left_half[p1]]>nums[right_half[p2]]:
                    ans.append(right_half[p2])
                    count+=1
                    p2+=1
                else:
                    ans.append(left_half[p1])
                    res[left_half[p1]]+=count
                    p1+=1
            while p1<len(left_half):
              ans.append(left_half[p1])
              res[left_half[p1]]+=count
              p1+=1
            while p2<len(right_half):
                ans.append(right_half[p2])
                p2+=1
            return ans

        def merge_sort(left,right,arr):

            if left==right:
                return [arr[left]]

            mid=left + (right-left)//2

            left_half=merge_sort(left,mid,arr)
            right_half=merge_sort(mid+1,right,arr)

            return merge(left_half,right_half)

        merge_sort(0,len(nums)-1,indexes)

        return res
        