# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().findAnagrams(s, p)
    print("\noutput:", serialize(ans, "integer[]"))
