# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/crawler-log-folder/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    logs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minOperations(logs)
    print("\noutput:", serialize(ans, "integer"))
