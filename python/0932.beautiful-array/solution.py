# Created by asetti2002 at 2024/04/25 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/beautiful-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def helper(arr):
            if len(arr) <= 2:
                return arr
            odd = [i * 2 - 1 for i in helper((arr + 1) // 2)]
            even = [i * 2 for i in helper(arr // 2)]
            return odd + even
        
        return helper(list(range(1, n + 1))
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().beautifulArray(n)
    print("\noutput:", serialize(ans, "integer[]"))
