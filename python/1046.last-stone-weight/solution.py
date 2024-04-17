# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/last-stone-weight/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lastStoneWeight(stones)
    print("\noutput:", serialize(ans, "integer"))
