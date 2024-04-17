# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/find-all-people-with-secret/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    meetings: List[List[int]] = deserialize("List[List[int]]", read_line())
    firstPerson: int = deserialize("int", read_line())
    ans = Solution().findAllPeople(n, meetings, firstPerson)
    print("\noutput:", serialize(ans, "integer[]"))
