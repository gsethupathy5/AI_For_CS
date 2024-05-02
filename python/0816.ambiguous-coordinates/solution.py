# Created by asetti2002 at 2024/04/25 19:07
# leetgo: 1.4.3
# https://leetcode.com/problems/ambiguous-coordinates/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def valid_nums(s):
            if s == "0" or s[0] != "0":
                yield s
            for i in range(1, len(s)):
                if (s[:i] == "0" or s[0] != "0") and (s[-1] != "0" or s[i:] == "0"):
                    yield s[:i] + ("." if i != len(s) else "") + s[i:]
        
        s = s[1:-1]
        n = len(s)
        res = []
        
        for i in range(1, n):
            for a, b in itertools.product(valid_nums(s[:i]), valid_nums(s[i:])):
                res.append(f"({a}, {b})")
        
        return res
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().ambiguousCoordinates(s)
    print("\noutput:", serialize(ans, "string[]"))
