# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestNumber(self, num: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().smallestNumber(num)
    print("\noutput:", serialize(ans, "long"))
