# Created by asetti2002 at 2024/04/25 20:28
# leetgo: 1.4.3
# https://leetcode.com/problems/verbal-arithmetic-puzzle/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        pass
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    result: str = deserialize("str", read_line())
    ans = Solution().isSolvable(words, result)
    print("\noutput:", serialize(ans, "boolean"))
