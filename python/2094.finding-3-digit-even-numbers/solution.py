# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/finding-3-digit-even-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    digits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findEvenNumbers(digits)
    print("\noutput:", serialize(ans, "integer[]"))
