# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-recent-calls/

from typing import *
from leetgo_py import *

# @lc code=begin

class RecentCounter:

    def __init__(self):
        

    def ping(self, t: int) -> int:
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = RecentCounter()

    for i in range(1, len(ops)):
        match ops[i]:
            case "ping":
                method_params = split_array(params[i])
                t: int = deserialize("int", method_params[0])
                ans = serialize(obj.ping(t))
                output.append(ans)

    print("\noutput:", join_array(output))
