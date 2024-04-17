# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-texts/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    pressedKeys: str = deserialize("str", read_line())
    ans = Solution().countTexts(pressedKeys)
    print("\noutput:", serialize(ans, "integer"))
