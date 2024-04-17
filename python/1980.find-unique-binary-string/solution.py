# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-unique-binary-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findDifferentBinaryString(nums)
    print("\noutput:", serialize(ans, "string"))
