# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().replaceNonCoprimes(nums)
    print("\noutput:", serialize(ans, "integer[]"))