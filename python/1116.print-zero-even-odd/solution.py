# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/print-zero-even-odd/

from typing import *
from leetgo_py import *

# @lc code=begin

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        
        
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().printZeroEvenOdd(n)
    print("\noutput:", serialize(ans, "integer"))
