class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1

        while start <= end:
            mid = (start+end) // 2

            if start == mid == end :
                return nums[mid]
            elif nums[mid] < nums[end] :
                end = mid
            else:
                start=mid+1
        