# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().divisibilityArray(word, m)
    print("\noutput:", serialize(ans, "integer[]"))
