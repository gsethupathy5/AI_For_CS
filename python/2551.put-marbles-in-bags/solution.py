# Created by asetti2002 at 2024/05/01 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/put-marbles-in-bags/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        weights.sort()
        return sum(weights[k-1:]) - sum(weights[:k-1])
# @lc code=end

if __name__ == "__main__":
    weights: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().putMarbles(weights, k)
    print("\noutput:", serialize(ans, "long"))
