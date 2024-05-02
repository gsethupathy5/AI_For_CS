# Created by asetti2002 at 2024/04/25 19:32
# leetgo: 1.4.3
# https://leetcode.com/problems/prime-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        
        n += 1
        while True:
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().primePalindrome(n)
    print("\noutput:", serialize(ans, "integer"))
