import re
class Solution(object):
    def myAtoi(self, str):
        r = ""
        if re.match("[ ]*[-+]?\d+", str):
            r = re.search("(-?\d+)", str);
        if r:
            return max(-2147483648, min(2147483647, int(r.group(1))))
        return 0
        
if __name__ == "__main__":
    solution = Solution()
    
    print solution.myAtoi("  -0012a42")