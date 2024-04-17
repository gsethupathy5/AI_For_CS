# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/online-election/

from typing import *
from leetgo_py import *

# @lc code=begin

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        

    def q(self, t: int) -> int:
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    persons: List[int] = deserialize("List[int]", constructor_params[0])
    times: List[int] = deserialize("List[int]", constructor_params[1])
    obj = TopVotedCandidate(persons, times)

    for i in range(1, len(ops)):
        match ops[i]:
            case "q":
                method_params = split_array(params[i])
                t: int = deserialize("int", method_params[0])
                ans = serialize(obj.q(t))
                output.append(ans)

    print("\noutput:", join_array(output))
