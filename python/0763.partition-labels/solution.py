# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-labels/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partitionLabels(s)
    print("\noutput:", serialize(ans, "integer[]"))