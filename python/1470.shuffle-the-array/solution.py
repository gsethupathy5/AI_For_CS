# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/shuffle-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().shuffle(nums, n)
    print("\noutput:", serialize(ans, "integer[]"))
