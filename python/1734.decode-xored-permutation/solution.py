# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/decode-xored-permutation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    encoded: List[int] = deserialize("List[int]", read_line())
    ans = Solution().decode(encoded)
    print("\noutput:", serialize(ans, "integer[]"))
