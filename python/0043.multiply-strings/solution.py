# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/multiply-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num1: str = deserialize("str", read_line())
    num2: str = deserialize("str", read_line())
    ans = Solution().multiply(num1, num2)
    print("\noutput:", serialize(ans, "string"))
