# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-the-jumbled-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    mapping: List[int] = deserialize("List[int]", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortJumbled(mapping, nums)
    print("\noutput:", serialize(ans, "integer[]"))
