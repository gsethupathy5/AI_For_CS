# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    security: List[int] = deserialize("List[int]", read_line())
    time: int = deserialize("int", read_line())
    ans = Solution().goodDaysToRobBank(security, time)
    print("\noutput:", serialize(ans, "integer[]"))
