# Created by asetti2002 at 2024/04/25 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        target_sum = total_sum // 3
        part_sum = 0
        count = 0
        for num in arr:
            part_sum += num
            if part_sum == target_sum:
                part_sum = 0
                count += 1
            if count == 3:
                return True
        return False
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canThreePartsEqualSum(arr)
    print("\noutput:", serialize(ans, "boolean"))
