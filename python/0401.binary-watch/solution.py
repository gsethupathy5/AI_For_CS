# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-watch/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    turnedOn: int = deserialize("int", read_line())
    ans = Solution().readBinaryWatch(turnedOn)
    print("\noutput:", serialize(ans, "string[]"))