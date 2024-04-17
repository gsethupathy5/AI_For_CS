# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    logs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().reorderLogFiles(logs)
    print("\noutput:", serialize(ans, "string[]"))
