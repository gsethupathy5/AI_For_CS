# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/long-pressed-name/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    name: str = deserialize("str", read_line())
    typed: str = deserialize("str", read_line())
    ans = Solution().isLongPressedName(name, typed)
    print("\noutput:", serialize(ans, "boolean"))
