# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/valid-arrangement-of-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    pairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().validArrangement(pairs)
    print("\noutput:", serialize(ans, "integer[][]"))
