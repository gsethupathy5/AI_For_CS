# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/russian-doll-envelopes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    envelopes: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxEnvelopes(envelopes)
    print("\noutput:", serialize(ans, "integer"))
