class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=(len(nums1)+len(nums2))
        m1=(n+1)/2-1
        m2=(n+1)//2-1

        nums1.extend(nums2)
        nums1.sort()
        x=int(m1)
        if m1==float(m2):
            return nums1[x]
        else:
            return (nums1[x]+nums1[x+1])/2
