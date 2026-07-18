class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums=set(nums)
        longest=0
        leng=0
        for i in setnums:
            if i-1 not in setnums:
                leng=1
                while i+1 in setnums:
                    leng+=1
                    i+=1
                longest=max(longest,leng)
        return longest

        