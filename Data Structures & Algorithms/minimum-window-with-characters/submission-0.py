class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i in t:
            need[i] = need.get(i,0)+1

        window = {}
        have = 0
        required = len(need)

        ans=""
        min_length = float("inf")
        
        left = 0
        
        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char,0)+1

            if char in need  and window[char] == need[char]:
                have += 1
            
            while have == required:
                if right - left + 1 < min_length :
                    min_length = right - left + 1
                    ans = s[left:right+1]

                left_char = s[left]

                window[left_char]-=1

                if left_char in need and window[left_char] < need[left_char] :
                    have -= 1
                
                left += 1
        
        return ans
