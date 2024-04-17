# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/apply-discount-every-n-orders/

from typing import *
from leetgo_py import *

# @lc code=begin

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    discount: int = deserialize("int", constructor_params[1])
    products: List[int] = deserialize("List[int]", constructor_params[2])
    prices: List[int] = deserialize("List[int]", constructor_params[3])
    obj = Cashier(n, discount, products, prices)

    for i in range(1, len(ops)):
        match ops[i]:
            case "getBill":
                method_params = split_array(params[i])
                product: List[int] = deserialize("List[int]", method_params[0])
                amount: List[int] = deserialize("List[int]", method_params[1])
                ans = serialize(obj.getBill(product, amount))
                output.append(ans)

    print("\noutput:", join_array(output))
