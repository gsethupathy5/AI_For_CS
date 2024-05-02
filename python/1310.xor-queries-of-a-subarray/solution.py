# Created by asetti2002 at 2024/04/25 20:29
# leetgo: 1.4.3
# https://leetcode.com/problems/xor-queries-of-a-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_values = []
        for query in queries:
            left = query[0]
            right = query[1]
            xor_val = arr[left]
            for i in range(left+1, right+1):
                xor_val ^= arr[i]
            xor_values.append(xor_val)
        return xor_values
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().xorQueries(arr, queries)
    print("\noutput:", serialize(ans, "integer[]"))
