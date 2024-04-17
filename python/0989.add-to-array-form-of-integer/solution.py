# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/add-to-array-form-of-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    num: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().addToArrayForm(num, k)
    print("\noutput:", serialize(ans, "integer[]"))
