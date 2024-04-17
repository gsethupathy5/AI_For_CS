# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-repeating-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    sequence: str = deserialize("str", read_line())
    word: str = deserialize("str", read_line())
    ans = Solution().maxRepeating(sequence, word)
    print("\noutput:", serialize(ans, "integer"))
