# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    ans = Solution().checkIfPangram(sentence)
    print("\noutput:", serialize(ans, "boolean"))
