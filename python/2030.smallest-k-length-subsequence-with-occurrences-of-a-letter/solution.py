# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    letter: str = deserialize("str", read_line())
    repetition: int = deserialize("int", read_line())
    ans = Solution().smallestSubsequence(s, k, letter, repetition)
    print("\noutput:", serialize(ans, "string"))
