# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/ransom-note/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    ransomNote: str = deserialize("str", read_line())
    magazine: str = deserialize("str", read_line())
    ans = Solution().canConstruct(ransomNote, magazine)
    print("\noutput:", serialize(ans, "boolean"))
