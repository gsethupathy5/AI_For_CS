# Created by asetti2002 at 2024/05/01 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        employee_times = [0] * n
        for i in range(1, len(logs)):
            employee_times[logs[i][0]] += logs[i][1] - logs[i-1][1]
        return employee_times.index(max(employee_times))
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    logs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().hardestWorker(n, logs)
    print("\noutput:", serialize(ans, "integer"))
