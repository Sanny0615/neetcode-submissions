class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=0
        st=set()
        ans=0
        for r in range(len(s)):
            while s[r] in st:
                st.discard(s[l])
                l+=1
            st.add(s[r])
            ans=max(ans,len(st))
        return ans

        