# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/employee-importance/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    employees: List[str] = deserialize("List[str]", read_line())
    id: int = deserialize("int", read_line())
    ans = Solution().getImportance(employees, id)
    print("\noutput:", serialize(ans, "integer"))
