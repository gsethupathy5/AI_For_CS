# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().vowelStrings(words, queries)
    print("\noutput:", serialize(ans, "integer[]"))
