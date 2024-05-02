# Created by asetti2002 at 2024/05/01 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def is_valid(subarray):
            if len(subarray) == 2:
                return subarray[0] == subarray[1]
            elif len(subarray) == 3:
                return subarray[0] == subarray[1] == subarray[2]
            else:
                return all(subarray[i] == subarray[i-1] + 1 for i in range(1, len(subarray)))
        
        for i in range(2, len(nums)):
            if is_valid(nums[:i]) and is_valid(nums[i:]):
                return True
        return False
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))
