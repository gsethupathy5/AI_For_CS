# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    a: str = deserialize("str", read_line())
    b: str = deserialize("str", read_line())
    ans = Solution().minCharacters(a, b)
    print("\noutput:", serialize(ans, "integer"))
