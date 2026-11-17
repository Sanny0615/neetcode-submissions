class Solution:
    def search(self, n: List[int], t: int) -> int:
        s=0
        e=len(n)-1
        while s<=e:
            m=(s+e)//2
            if n[m]==t:
                return m
            elif n[s]<=n[m]:
                if n[s]<=t and t<=n[m]:
                    e=m-1
                else:
                    s=m+1
            else:
                if n[m]<=t and t<=n[e]:
                    s=m+1
                else:
                    e=m-1
        return -1

        