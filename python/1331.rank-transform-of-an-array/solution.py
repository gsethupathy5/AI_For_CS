# Created by asetti2002 at 2024/04/25 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/rank-transform-of-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().arrayRankTransform(arr)
    print("\noutput:", serialize(ans, "integer[]"))
