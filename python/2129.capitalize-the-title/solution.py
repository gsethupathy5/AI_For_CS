# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/capitalize-the-title/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    title: str = deserialize("str", read_line())
    ans = Solution().capitalizeTitle(title)
    print("\noutput:", serialize(ans, "string"))
