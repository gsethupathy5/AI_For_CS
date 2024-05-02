# Created by asetti2002 at 2024/05/01 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-bad-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i < j and j - i != nums[j] - nums[i]:
                    count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countBadPairs(nums)
    print("\noutput:", serialize(ans, "long"))
