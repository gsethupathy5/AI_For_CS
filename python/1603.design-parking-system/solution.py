# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/design-parking-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        

    def addCar(self, carType: int) -> bool:
        

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    big: int = deserialize("int", constructor_params[0])
    medium: int = deserialize("int", constructor_params[1])
    small: int = deserialize("int", constructor_params[2])
    obj = ParkingSystem(big, medium, small)

    for i in range(1, len(ops)):
        match ops[i]:
            case "addCar":
                method_params = split_array(params[i])
                carType: int = deserialize("int", method_params[0])
                ans = serialize(obj.addCar(carType))
                output.append(ans)

    print("\noutput:", join_array(output))
