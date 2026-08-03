class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            r=[]
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s==0:
                    r=[nums[i],nums[left],nums[right]]
                    l.append(r)
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left+=1
                else:
                    right-=1
                
        return l
                    