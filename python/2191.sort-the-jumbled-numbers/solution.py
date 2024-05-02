# Created by asetti2002 at 2024/04/25 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-the-jumbled-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: ''.join(str(mapping[int(i)]) for i in str(x)))
        return nums
# @lc code=end

if __name__ == "__main__":
    mapping: List[int] = deserialize("List[int]", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortJumbled(mapping, nums)
    print("\noutput:", serialize(ans, "integer[]"))
