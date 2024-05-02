# Created by asetti2002 at 2024/05/01 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-excellent-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if bin(nums[i] & nums[j]).count('1') + bin(nums[i] | nums[j]).count('1') >= k:
                    count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countExcellentPairs(nums, k)
    print("\noutput:", serialize(ans, "long"))
