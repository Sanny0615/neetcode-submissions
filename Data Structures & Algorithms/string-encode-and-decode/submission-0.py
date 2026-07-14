class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        c=0
        for i in range(len(strs)):
            s+=str(len(strs[i]))+"#"+strs[i]
        return s
            




    def decode(self, s: str) -> List[str]:
        decode_string=[]
        sn=""
        n=0
        i=0
        while i<len(s):
            if s[i]=="#":
                n=int(sn)
                sn=""
                decode_string.append(s[i+1:i+n+1])
                i+=n+1
                n=0
            else:
                sn+=s[i]
                i+=1
        return decode_string
