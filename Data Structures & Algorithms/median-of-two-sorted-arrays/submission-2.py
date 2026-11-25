class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        x = n // 2

        if n % 2 == 0:
            l = [x, x + 1]
        else:
            l = [x + 1]

        i = 0
        j = 0
        count = 0
        total = 0

        while count < x + 1:
            if i >= len(nums1):
                current = nums2[j]
                j += 1

            elif j >= len(nums2):
                current = nums1[i]
                i += 1

            else:
                if nums1[i] < nums2[j]:
                    current = nums1[i]
                    i += 1
                else:
                    current = nums2[j]
                    j += 1

            count += 1

            if count in l:
                total += current

        if n % 2 == 0:
            return total / 2
        else:
            return total