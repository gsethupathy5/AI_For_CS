# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    digits: List[str] = deserialize("List[str]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().atMostNGivenDigitSet(digits, n)
    print("\noutput:", serialize(ans, "integer"))
