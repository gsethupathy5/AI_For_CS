# Created by asetti2002 at 2024/04/25 19:02
# leetgo: 1.4.3
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        import random
        result = sorted(nums)
        while True:
            random.shuffle(result)
            valid = True
            for i in range(1, len(result) - 1):
                if (result[i-1] + result[i+1]) / 2 == result[i]:
                    valid = False
                    break
            if valid:
                return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rearrangeArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
