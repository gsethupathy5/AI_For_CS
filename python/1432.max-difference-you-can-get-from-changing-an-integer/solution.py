# Created by asetti2002 at 2024/04/25 20:41
# leetgo: 1.4.3
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        a = max(int(s.replace(d, '9') for d in s if d != '0'))
        b = min(int(s.replace(d, '1') for d in s[0] + s[1:] if d != s[0]))
        return a - b
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().maxDiff(num)
    print("\noutput:", serialize(ans, "integer"))
