# Created by asetti2002 at 2024/04/25 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/the-dining-philosophers/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        pass
# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    ans = Solution().foobar(target)
    print("\noutput:", serialize(ans, "integer"))
