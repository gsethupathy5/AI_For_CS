# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/palindrome-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().palindromePairs(words)
    print("\noutput:", serialize(ans, "integer[][]"))
