# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/find-missing-observations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    rolls: List[int] = deserialize("List[int]", read_line())
    mean: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().missingRolls(rolls, mean, n)
    print("\noutput:", serialize(ans, "integer[]"))
