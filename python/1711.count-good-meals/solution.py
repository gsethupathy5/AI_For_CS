# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/count-good-meals/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    deliciousness: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countPairs(deliciousness)
    print("\noutput:", serialize(ans, "integer"))
