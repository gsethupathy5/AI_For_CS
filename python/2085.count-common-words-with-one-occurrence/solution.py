# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/count-common-words-with-one-occurrence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words1: List[str] = deserialize("List[str]", read_line())
    words2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().countWords(words1, words2)
    print("\noutput:", serialize(ans, "integer"))