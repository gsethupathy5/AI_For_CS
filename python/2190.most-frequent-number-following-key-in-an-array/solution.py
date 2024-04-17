# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    key: int = deserialize("int", read_line())
    ans = Solution().mostFrequent(nums, key)
    print("\noutput:", serialize(ans, "integer"))
