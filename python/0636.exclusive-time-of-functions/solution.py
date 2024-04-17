# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/exclusive-time-of-functions/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    logs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().exclusiveTime(n, logs)
    print("\noutput:", serialize(ans, "integer[]"))
