# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/stock-price-fluctuation/

from typing import *
from leetgo_py import *

# @lc code=begin

class StockPrice:

    def __init__(self):
        

    def update(self, timestamp: int, price: int) -> None:
        

    def current(self) -> int:
        

    def maximum(self) -> int:
        

    def minimum(self) -> int:
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = StockPrice()

    for i in range(1, len(ops)):
        match ops[i]:
            case "update":
                method_params = split_array(params[i])
                timestamp: int = deserialize("int", method_params[0])
                price: int = deserialize("int", method_params[1])
                obj.update(timestamp, price)
                output.append("null")
            case "current":
                ans = serialize(obj.current())
                output.append(ans)
            case "maximum":
                ans = serialize(obj.maximum())
                output.append(ans)
            case "minimum":
                ans = serialize(obj.minimum())
                output.append(ans)

    print("\noutput:", join_array(output))
