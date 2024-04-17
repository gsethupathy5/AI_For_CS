# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-hidden-sequences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    differences: List[int] = deserialize("List[int]", read_line())
    lower: int = deserialize("int", read_line())
    upper: int = deserialize("int", read_line())
    ans = Solution().numberOfArrays(differences, lower, upper)
    print("\noutput:", serialize(ans, "integer"))
