class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if len(s)!=len(t):
            return False
        for ch1, ch2 in zip(s, t):
            d1[ch1] = d1.get(ch1, 0) + 1
            d2[ch2] = d2.get(ch2, 0) + 1
        return d1==d2