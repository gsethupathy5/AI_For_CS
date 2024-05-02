# Created by asetti2002 at 2024/05/01 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/pass-the-pillow/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        while time > 0:
            if time % (2*(n-1)) < n:
                return time % (2*(n-1)) + 1
            time -= n - 1 - time % (n-1)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    time: int = deserialize("int", read_line())
    ans = Solution().passThePillow(n, time)
    print("\noutput:", serialize(ans, "integer"))
