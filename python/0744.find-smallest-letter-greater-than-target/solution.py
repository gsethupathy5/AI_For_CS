# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    letters: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().nextGreatestLetter(letters, target)
    print("\noutput:", serialize(ans, "character"))
