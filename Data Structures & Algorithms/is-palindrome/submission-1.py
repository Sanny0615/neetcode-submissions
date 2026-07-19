class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = []

        for ch in s:
            if ch.isalnum():
                p.append(ch.lower())

        p = "".join(p)
        left=0
        right=len(p)-1
        while left<right:
            if p[left]!=p[right]:
                return False
            left+=1
            right-=1
        return True

        