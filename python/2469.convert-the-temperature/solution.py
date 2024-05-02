# Created by asetti2002 at 2024/05/01 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/convert-the-temperature/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [round(kelvin, 5), round(fahrenheit, 5)]
# @lc code=end

if __name__ == "__main__":
    celsius: float = deserialize("float", read_line())
    ans = Solution().convertTemperature(celsius)
    print("\noutput:", serialize(ans, "double[]"))
