# Created by asetti2002 at 2024/05/01 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/count-anagrams/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countAnagrams(self, s: str) -> int:
        return 0  # Placeholder for the actual implementation
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countAnagrams(s)
    print("\noutput:", serialize(ans, "integer"))
