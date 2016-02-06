class Solution(object):
    def lengthOfLongestSubstring(self, s):
        L, res, lastAppear = -1, 0, [-1] * 128
        for R in range(len(s)):
            pos = ord(s[R])
            if lastAppear[pos] > L:
                L = lastAppear[pos]
            else:
                res = max(res, R - L)
            lastAppear[pos] = R
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print solution.lengthOfLongestSubstring("abcabcbb")