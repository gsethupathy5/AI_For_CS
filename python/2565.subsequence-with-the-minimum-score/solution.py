# Created by asetti2002 at 2024/05/01 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/subsequence-with-the-minimum-score/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        def binarySearch():
            pass

        return 0
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minimumScore(s, t)
    print("\noutput:", serialize(ans, "integer"))
