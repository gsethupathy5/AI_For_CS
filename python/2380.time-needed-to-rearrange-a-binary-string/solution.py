# Created by asetti2002 at 2024/05/01 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        while '01' in s:
            s = s.replace('01', '10')
            count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().secondsToRemoveOccurrences(s)
    print("\noutput:", serialize(ans, "integer"))
