# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def equalFrequency(self, word: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().equalFrequency(word)
    print("\noutput:", serialize(ans, "boolean"))
