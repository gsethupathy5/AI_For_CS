# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/building-h2o/

from typing import *
from leetgo_py import *

# @lc code=begin

class H2O:
    def __init__(self):
        pass

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    water: str = deserialize("str", read_line())
    ans = Solution().H2O(water)
    print("\noutput:", serialize(ans, "string"))
