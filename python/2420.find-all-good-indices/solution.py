# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/find-all-good-indices/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        def is_good(i):
            return all(nums[i - k: i] >= nums[i - k + 1: i + 1]) and all(nums[i: i + k] <= nums[i + 1: i + k + 1])
        
        return [i for i in range(k, len(nums) - k) if is_good(i)]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().goodIndices(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
