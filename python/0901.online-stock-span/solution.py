# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/online-stock-span/

from typing import *
from leetgo_py import *

# @lc code=begin

class StockSpanner:

    def __init__(self):
        

    def next(self, price: int) -> int:
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = StockSpanner()

    for i in range(1, len(ops)):
        match ops[i]:
            case "next":
                method_params = split_array(params[i])
                price: int = deserialize("int", method_params[0])
                ans = serialize(obj.next(price))
                output.append(ans)

    print("\noutput:", join_array(output))
