# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/single-threaded-cpu/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    tasks: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getOrder(tasks)
    print("\noutput:", serialize(ans, "integer[]"))
