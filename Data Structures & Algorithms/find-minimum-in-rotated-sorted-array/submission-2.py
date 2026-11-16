class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1

        while start <= end:
            mid = (start+end)//2

            if start == mid and  end == mid:
                return nums[mid]
            elif nums[start]<nums[mid]:
                if nums[start]<nums[end]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<nums[end]:
                    end=mid
                else:
                    start=mid+1
        return -1