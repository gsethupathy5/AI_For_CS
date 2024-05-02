# Created by asetti2002 at 2024/05/01 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/closest-prime-numbers-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin
import math
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        def find_next_prime(num):
            while True:
                num += 1
                if is_prime(num):
                    return num
        
        def find_previous_prime(num):
            while True:
                num -= 1
                if is_prime(num):
                    return num
        
        if right - left < 1:
            return [-1, -1]
        
        start = left
        while True:
            if is_prime(start):
                break
            start += 1
        
        prime1 = start
        prime2 = find_next_prime(start)
        
        while prime2 <= right and not(is_prime(prime2)):
            prime2 = find_next_prime(prime2)
        
        while prime1 >= left and not(is_prime(prime1)):
            prime1 = find_previous_prime(prime1)
        
        if prime2 > right or prime1 < left:
            return [-1, -1]
        
        return [prime1, prime2]
# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().closestPrimes(left, right)
    print("\noutput:", serialize(ans, "integer[]"))
