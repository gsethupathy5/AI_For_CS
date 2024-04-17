# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/bulls-and-cows/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    secret: str = deserialize("str", read_line())
    guess: str = deserialize("str", read_line())
    ans = Solution().getHint(secret, guess)
    print("\noutput:", serialize(ans, "string"))
