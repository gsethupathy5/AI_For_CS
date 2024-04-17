# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/bag-of-tokens/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tokens: List[int] = deserialize("List[int]", read_line())
    power: int = deserialize("int", read_line())
    ans = Solution().bagOfTokensScore(tokens, power)
    print("\noutput:", serialize(ans, "integer"))
