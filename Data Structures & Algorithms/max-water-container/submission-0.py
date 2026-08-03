class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        area=0
        max_area=0
        while left<right:
            H=min(heights[left],heights[right])
            W=right-left
            area=H*W
            max_area=max(area,max_area)
            if H==heights[left]:
                left+=1
            else:
                right-=1
        return max_area