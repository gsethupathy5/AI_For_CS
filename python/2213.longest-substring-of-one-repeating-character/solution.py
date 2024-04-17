# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    queryCharacters: str = deserialize("str", read_line())
    queryIndices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestRepeating(s, queryCharacters, queryIndices)
    print("\noutput:", serialize(ans, "integer[]"))
