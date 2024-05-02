# Created by asetti2002 at 2024/04/25 20:03
# leetgo: 1.4.3
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove_count = len(arr) // 20
        trimmed_arr = arr[remove_count:-remove_count]
        return sum(trimmed_arr) / len(trimmed_arr)
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trimMean(arr)
    print("\noutput:", serialize(ans, "double"))
