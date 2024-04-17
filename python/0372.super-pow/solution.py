# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/super-pow/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: List[int] = deserialize("List[int]", read_line())
    ans = Solution().superPow(a, b)
    print("\noutput:", serialize(ans, "integer"))
