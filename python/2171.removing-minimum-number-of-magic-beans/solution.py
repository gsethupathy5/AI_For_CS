# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    beans: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRemoval(beans)
    print("\noutput:", serialize(ans, "long"))
