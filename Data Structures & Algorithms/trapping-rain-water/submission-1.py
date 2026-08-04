class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for i in range(1, len(height)-1):

            leftMax = height[i]
            for l in range(i):
                leftMax = max(leftMax, height[l])

            rightMax = height[i]
            for r in range(i+1, len(height)):
                rightMax = max(rightMax, height[r])

            water += min(leftMax, rightMax) - height[i]

        return water