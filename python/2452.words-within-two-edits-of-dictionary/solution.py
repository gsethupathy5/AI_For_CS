# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    queries: List[str] = deserialize("List[str]", read_line())
    dictionary: List[str] = deserialize("List[str]", read_line())
    ans = Solution().twoEditWords(queries, dictionary)
    print("\noutput:", serialize(ans, "string[]"))
