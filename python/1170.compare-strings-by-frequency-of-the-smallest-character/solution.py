# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    queries: List[str] = deserialize("List[str]", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numSmallerByFrequency(queries, words)
    print("\noutput:", serialize(ans, "integer[]"))
