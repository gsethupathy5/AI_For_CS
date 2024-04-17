# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-completing-word/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    licensePlate: str = deserialize("str", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().shortestCompletingWord(licensePlate, words)
    print("\noutput:", serialize(ans, "string"))
