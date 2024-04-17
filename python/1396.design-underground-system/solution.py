# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/design-underground-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class UndergroundSystem:

    def __init__(self):
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = UndergroundSystem()

    for i in range(1, len(ops)):
        match ops[i]:
            case "checkIn":
                method_params = split_array(params[i])
                id: int = deserialize("int", method_params[0])
                stationName: str = deserialize("str", method_params[1])
                t: int = deserialize("int", method_params[2])
                obj.checkIn(id, stationName, t)
                output.append("null")
            case "checkOut":
                method_params = split_array(params[i])
                id: int = deserialize("int", method_params[0])
                stationName: str = deserialize("str", method_params[1])
                t: int = deserialize("int", method_params[2])
                obj.checkOut(id, stationName, t)
                output.append("null")
            case "getAverageTime":
                method_params = split_array(params[i])
                startStation: str = deserialize("str", method_params[0])
                endStation: str = deserialize("str", method_params[1])
                ans = serialize(obj.getAverageTime(startStation, endStation))
                output.append(ans)

    print("\noutput:", join_array(output))
