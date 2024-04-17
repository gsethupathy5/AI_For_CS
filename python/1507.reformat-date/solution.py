# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/reformat-date/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reformatDate(self, date: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    date: str = deserialize("str", read_line())
    ans = Solution().reformatDate(date)
    print("\noutput:", serialize(ans, "string"))
