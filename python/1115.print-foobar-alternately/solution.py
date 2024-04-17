# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/print-foobar-alternately/

from typing import *
from leetgo_py import *

# @lc code=begin

class FooBar:
    def __init__(self, n):
        self.n = n

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().FooBar(n)
    print("\noutput:", serialize(ans, "integer"))
