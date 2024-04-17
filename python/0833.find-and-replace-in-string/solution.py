# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/find-and-replace-in-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    indices: List[int] = deserialize("List[int]", read_line())
    sources: List[str] = deserialize("List[str]", read_line())
    targets: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findReplaceString(s, indices, sources, targets)
    print("\noutput:", serialize(ans, "string"))
