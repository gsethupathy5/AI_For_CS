# Created by asetti2002 at 2024/05/01 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + strength[i]
        
        stack = []
        total_strength = 0
        
        for i in range(n):
            while stack and strength[i] < strength[stack[-1]]:
                j = stack.pop()
                total_strength += (prefix_sum[i] - prefix_sum[j]) * strength[j]
                total_strength %= MOD
            stack.append(i)
        
        while stack:
            j = stack.pop()
            total_strength += (prefix_sum[n] - prefix_sum[j]) * strength[j]
            total_strength %= MOD
        
        return total_strength
# @lc code=end

if __name__ == "__main__":
    strength: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalStrength(strength)
    print("\noutput:", serialize(ans, "integer"))
