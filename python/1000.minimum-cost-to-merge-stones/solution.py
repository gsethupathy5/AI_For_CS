# Created by asetti2002 at 2024/04/25 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-merge-stones/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().mergeStones(stones, k)
    print("\noutput:", serialize(ans, "integer"))
