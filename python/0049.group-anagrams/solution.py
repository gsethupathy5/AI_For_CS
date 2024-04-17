# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/group-anagrams/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
