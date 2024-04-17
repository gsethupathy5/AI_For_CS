# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/print-in-order/

from typing import *
from leetgo_py import *

# @lc code=begin

class Foo:
    def __init__(self):
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().foobar(nums)
    print("\noutput:", serialize(ans, "integer"))
