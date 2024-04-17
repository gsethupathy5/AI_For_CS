# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/convert-the-temperature/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        

# @lc code=end

if __name__ == "__main__":
    celsius: float = deserialize("float", read_line())
    ans = Solution().convertTemperature(celsius)
    print("\noutput:", serialize(ans, "double[]"))
