# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkValid(matrix)
    print("\noutput:", serialize(ans, "boolean"))
