# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/design-an-atm-machine/

from typing import *
from leetgo_py import *

# @lc code=begin

class ATM:

    def __init__(self):
        

    def deposit(self, banknotesCount: List[int]) -> None:
        

    def withdraw(self, amount: int) -> List[int]:
        

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = ATM()

    for i in range(1, len(ops)):
        match ops[i]:
            case "deposit":
                method_params = split_array(params[i])
                banknotesCount: List[int] = deserialize("List[int]", method_params[0])
                obj.deposit(banknotesCount)
                output.append("null")
            case "withdraw":
                method_params = split_array(params[i])
                amount: int = deserialize("int", method_params[0])
                ans = serialize(obj.withdraw(amount))
                output.append(ans)

    print("\noutput:", join_array(output))
