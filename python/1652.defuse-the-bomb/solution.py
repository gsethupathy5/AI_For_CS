# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/defuse-the-bomb/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    code: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().decrypt(code, k)
    print("\noutput:", serialize(ans, "integer[]"))
