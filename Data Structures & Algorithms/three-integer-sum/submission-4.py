class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        
        nums.sort()
        for i in range(len(nums)):
            left=0
            right=len(nums)-1
            r=[]
            while left<right:
                if left==i:
                    left+=1
                    continue
                elif right==i:
                    right-=1
                    continue
                s=nums[i]+nums[left]+nums[right]
                if s==0:
                       r=[nums[i],nums[left],nums[right]]
                       r.sort()
                       if r not in l:
                        l.append(r)
                if s>0:
                    right-=1
                else:
                    left+=1
        return l
                    