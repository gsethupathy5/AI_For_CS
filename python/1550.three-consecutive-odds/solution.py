# Created by asetti2002 at 2024/04/25 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/three-consecutive-odds/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeConsecutiveOdds(arr)
    print("\noutput:", serialize(ans, "boolean"))
