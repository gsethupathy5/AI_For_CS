# Created by asetti2002 at 2024/04/25 19:41
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-subarrays-with-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum_dict = {0:1}
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            if cur_sum - goal in sum_dict:
                count += sum_dict[cur_sum - goal]
            if cur_sum in sum_dict:
                sum_dict[cur_sum] += 1
            else:
                sum_dict[cur_sum] = 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    goal: int = deserialize("int", read_line())
    ans = Solution().numSubarraysWithSum(nums, goal)
    print("\noutput:", serialize(ans, "integer"))
