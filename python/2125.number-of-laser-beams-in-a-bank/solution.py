# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    bank: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numberOfBeams(bank)
    print("\noutput:", serialize(ans, "integer"))
