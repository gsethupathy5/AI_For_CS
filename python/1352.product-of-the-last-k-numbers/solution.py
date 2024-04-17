# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/product-of-the-last-k-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class ProductOfNumbers:

    def __init__(self):
        

    def add(self, num: int) -> None:
        

    def getProduct(self, k: int) -> int:
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = ProductOfNumbers()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.add(num)
                output.append("null")
            case "getProduct":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                ans = serialize(obj.getProduct(k))
                output.append(ans)

    print("\noutput:", join_array(output))
