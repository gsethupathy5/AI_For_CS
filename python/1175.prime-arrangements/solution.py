# Created by asetti2002 at 2024/04/25 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/prime-arrangements/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True
        
        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result = (result * i) % MOD
            return result
        
        prime_count = sum(1 for i in range(1, n+1) if is_prime(i))
        non_prime_count = n - prime_count
        
        return (factorial(prime_count) * factorial(non_prime_count)) % MOD
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numPrimeArrangements(n)
    print("\noutput:", serialize(ans, "integer"))
