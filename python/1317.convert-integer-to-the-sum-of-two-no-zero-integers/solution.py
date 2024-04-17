# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().getNoZeroIntegers(n)
    print("\noutput:", serialize(ans, "integer[]"))
