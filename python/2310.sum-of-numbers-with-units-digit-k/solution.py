# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumNumbers(num, k)
    print("\noutput:", serialize(ans, "integer"))
