# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-length-of-pair-chain/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    pairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findLongestChain(pairs)
    print("\noutput:", serialize(ans, "integer"))
