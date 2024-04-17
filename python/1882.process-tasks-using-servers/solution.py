# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/process-tasks-using-servers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    servers: List[int] = deserialize("List[int]", read_line())
    tasks: List[int] = deserialize("List[int]", read_line())
    ans = Solution().assignTasks(servers, tasks)
    print("\noutput:", serialize(ans, "integer[]"))
