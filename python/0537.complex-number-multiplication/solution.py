# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/complex-number-multiplication/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num1: str = deserialize("str", read_line())
    num2: str = deserialize("str", read_line())
    ans = Solution().complexNumberMultiply(num1, num2)
    print("\noutput:", serialize(ans, "string"))
