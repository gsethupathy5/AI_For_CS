# Created by asetti2002 at 2024/04/25 19:41
# leetgo: 1.4.3
# https://leetcode.com/problems/long-pressed-name/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
        
        return i == len(name)
# @lc code=end

if __name__ == "__main__":
    name: str = deserialize("str", read_line())
    typed: str = deserialize("str", read_line())
    ans = Solution().isLongPressedName(name, typed)
    print("\noutput:", serialize(ans, "boolean"))
