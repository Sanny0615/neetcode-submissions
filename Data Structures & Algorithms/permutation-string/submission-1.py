class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        st1=sorted(s1)
        n=len(s1)
        l=0
        for r in range(n,len(s2)+1):
            st2=sorted(s2[l:r])
            if st2==st1:
                print(st2)
                return True
            l+=1
        return False
        