# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    loginTime: str = deserialize("str", read_line())
    logoutTime: str = deserialize("str", read_line())
    ans = Solution().numberOfRounds(loginTime, logoutTime)
    print("\noutput:", serialize(ans, "integer"))
