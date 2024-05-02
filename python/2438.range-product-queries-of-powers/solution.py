# Created by asetti2002 at 2024/05/01 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/range-product-queries-of-powers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = [1]
        for i in range(1, n.bit_length()):
            powers.append(powers[-1] * 2 % MOD)
            
        ans = []
        
        for query in queries:
            left, right = query[0], query[1]
            product = 1
            for i in range(left, right + 1):
                product = (product * powers[i]) % MOD
            ans.append(product)
            
        return ans
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().productQueries(n, queries)
    print("\noutput:", serialize(ans, "integer[]"))
