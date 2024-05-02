# Created by asetti2002 at 2024/04/25 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/circular-permutation-in-binary-representation/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def grayCode(n):
            return [i ^ (i >> 1) for i in range(2**n)]

        gray_code = grayCode(n)
        index = gray_code.index(start)

        return gray_code[index:] + gray_code[:index]
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().circularPermutation(n, start)
    print("\noutput:", serialize(ans, "integer[]"))
