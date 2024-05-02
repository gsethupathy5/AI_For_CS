# Created by asetti2002 at 2024/04/25 20:39
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a, b = 1, 1
        fib = [a, b]
        while b < k:
            a, b = b, a + b
            fib.append(b)
        count = 0
        while k > 0:
            while fib[-1] > k:
                fib.pop()
            k -= fib[-1]
            count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    ans = Solution().findMinFibonacciNumbers(k)
    print("\noutput:", serialize(ans, "integer"))
