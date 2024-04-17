# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/split-message-based-on-limit/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    message: str = deserialize("str", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().splitMessage(message, limit)
    print("\noutput:", serialize(ans, "string[]"))
