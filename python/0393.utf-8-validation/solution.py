# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/utf-8-validation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    data: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validUtf8(data)
    print("\noutput:", serialize(ans, "boolean"))
