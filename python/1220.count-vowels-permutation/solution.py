# Created by asetti2002 at 2024/04/25 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/count-vowels-permutation/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        for _ in range(1, n):
            a_next = (e + u + i) % MOD
            e_next = (a + i) % MOD
            i_next = (e + o) % MOD
            o_next = i % MOD
            u_next = (i + o) % MOD
            
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        
        return (a + e + i + o + u) % MOD
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countVowelPermutation(n)
    print("\noutput:", serialize(ans, "integer"))
