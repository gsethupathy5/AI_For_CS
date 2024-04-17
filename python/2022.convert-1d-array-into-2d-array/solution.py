# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/convert-1d-array-into-2d-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    original: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().construct2DArray(original, m, n)
    print("\noutput:", serialize(ans, "integer[][]"))
