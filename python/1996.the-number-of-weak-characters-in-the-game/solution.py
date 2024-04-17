# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    properties: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberOfWeakCharacters(properties)
    print("\noutput:", serialize(ans, "integer"))
