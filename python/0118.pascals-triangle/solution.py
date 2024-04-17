# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/pascals-triangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    numRows: int = deserialize("int", read_line())
    ans = Solution().generate(numRows)
    print("\noutput:", serialize(ans, "integer[][]"))
