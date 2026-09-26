class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        freq={}
        mxfq=0
        ans=0

        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            mxfq=max(mxfq,freq[s[right]])

            while (right-left+1)-mxfq>k:
                freq[s[left]]-=1
                left+=1

            ans=max(ans,right-left+1)

        return ans