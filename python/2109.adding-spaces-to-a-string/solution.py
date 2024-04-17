# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/adding-spaces-to-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    spaces: List[int] = deserialize("List[int]", read_line())
    ans = Solution().addSpaces(s, spaces)
    print("\noutput:", serialize(ans, "string"))
