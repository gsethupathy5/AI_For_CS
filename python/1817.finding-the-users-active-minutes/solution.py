# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/finding-the-users-active-minutes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    logs: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findingUsersActiveMinutes(logs, k)
    print("\noutput:", serialize(ans, "integer[]"))
