# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    chalk: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().chalkReplacer(chalk, k)
    print("\noutput:", serialize(ans, "integer"))
