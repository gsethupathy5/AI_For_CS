# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/count-ways-to-make-array-with-product/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().waysToFillArray(queries)
    print("\noutput:", serialize(ans, "integer[]"))
