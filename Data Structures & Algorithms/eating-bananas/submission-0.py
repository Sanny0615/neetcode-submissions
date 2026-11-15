class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = 0

        while start <= end:
            mid = (start+end)//2

            total=0

            for i in piles:
                total += (i//mid)
                if i%mid != 0:
                    total+=1
            if total <= h:
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
        