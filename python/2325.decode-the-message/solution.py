# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/decode-the-message/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    key: str = deserialize("str", read_line())
    message: str = deserialize("str", read_line())
    ans = Solution().decodeMessage(key, message)
    print("\noutput:", serialize(ans, "string"))
