class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(arr):
            seen=set()
            for val in arr:
                if val==".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
            return True
        val=0
        for i in range(9):
            if not check(board[i]):
                return False
            c=[]
            for j in range(9):
                val=board[j][i]
                c.append(val)
            if not check(c):
                return False
            
        for r_s in range(0,9,3):
            for c_s in range(0,9,3):
                c=[]
                for i in range(r_s,r_s+3):
                    for j in range(c_s,c_s+3):
                        val=board[i][j]
                        c.append(val)
                if not check(c):
                    return False
        return True