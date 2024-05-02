# Created by asetti2002 at 2024/04/25 20:36
# leetgo: 1.4.3
# https://leetcode.com/problems/time-needed-to-inform-all-employees/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict

        def dfs(employee):
            return informTime[employee] + max(dfs(subordinate) for subordinate in employees[employee])

        employees = defaultdict(list)
        for i, m in enumerate(manager):
            employees[m].append(i)

        return dfs(headID)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    headID: int = deserialize("int", read_line())
    manager: List[int] = deserialize("List[int]", read_line())
    informTime: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numOfMinutes(n, headID, manager, informTime)
    print("\noutput:", serialize(ans, "integer"))
