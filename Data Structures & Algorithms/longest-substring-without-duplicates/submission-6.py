class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=0
        st=set()
        st.add(s[0])
        ans=1
        for r in range(1,len(s)):
            while s[r] in st:
                st.discard(s[l])
                l+=1
            st.add(s[r])
            ans=max(ans,len(st))
        return ans

        