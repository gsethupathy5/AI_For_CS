# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    forts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().captureForts(forts)
    print("\noutput:", serialize(ans, "integer"))
