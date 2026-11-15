class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        left = 0
        column = len(m[0])
        right = len(m) * column -1
        while left <= right:
            mid = (left+right)//2
            row = mid // column
            col = mid % column

            if m[row][col] == target:
                return True
            elif m[row][col] < target:
                left = mid+1
            else:
                right = mid-1
        return False