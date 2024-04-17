# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    startIndex: int = deserialize("int", read_line())
    ans = Solution().closetTarget(words, target, startIndex)
    print("\noutput:", serialize(ans, "integer"))
