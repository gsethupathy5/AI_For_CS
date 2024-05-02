# Created by asetti2002 at 2024/04/25 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/di-string-match/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        res = []
        low, high = 0, n
        for c in s:
            if c == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append(high)
        return res
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().diStringMatch(s)
    print("\noutput:", serialize(ans, "integer[]"))
