class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        s_max = 0
        l = 0
        for i in range(len(s)):
            while s[i] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[i])
            s_max = max(s_max, i - l + 1)
        return s_max


# sol = Solution()
# node = sol.lengthOfLongestSubstring('bbbbb')
# print(node)

