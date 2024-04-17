# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/simple-bank-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class Bank:

    def __init__(self, balance: List[int]):
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        

    def deposit(self, account: int, money: int) -> bool:
        

    def withdraw(self, account: int, money: int) -> bool:
        

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    balance: List[int] = deserialize("List[int]", constructor_params[0])
    obj = Bank(balance)

    for i in range(1, len(ops)):
        match ops[i]:
            case "transfer":
                method_params = split_array(params[i])
                account1: int = deserialize("int", method_params[0])
                account2: int = deserialize("int", method_params[1])
                money: int = deserialize("int", method_params[2])
                ans = serialize(obj.transfer(account1, account2, money))
                output.append(ans)
            case "deposit":
                method_params = split_array(params[i])
                account: int = deserialize("int", method_params[0])
                money: int = deserialize("int", method_params[1])
                ans = serialize(obj.deposit(account, money))
                output.append(ans)
            case "withdraw":
                method_params = split_array(params[i])
                account: int = deserialize("int", method_params[0])
                money: int = deserialize("int", method_params[1])
                ans = serialize(obj.withdraw(account, money))
                output.append(ans)

    print("\noutput:", join_array(output))
