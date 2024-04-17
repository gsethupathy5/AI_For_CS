# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    keyName: List[str] = deserialize("List[str]", read_line())
    keyTime: List[str] = deserialize("List[str]", read_line())
    ans = Solution().alertNames(keyName, keyTime)
    print("\noutput:", serialize(ans, "string[]"))
