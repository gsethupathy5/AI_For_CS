# Created by asetti2002 at 2024/04/25 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/invalid-transactions/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        import collections
        names = collections.defaultdict(list)
        result = []
        
        for trans in transactions:
            name, time, amount, city = trans.split(',')
            time = int(time)
            amount = int(amount)
            
            if amount > 1000:
                result.append(trans)
            
            else:
                for prev_trans in names[name]:
                    prev_name, prev_time, prev_amount, prev_city = prev_trans.split(',')
                    prev_time = int(prev_time)
                    prev_amount = int(prev_amount)
                    if abs(time - prev_time) <= 60 and city != prev_city:
                        result.append(trans)
                        result.append(prev_trans)
            
            names[name].append(trans)
        
        return list(set(result))
# @lc code=end

if __name__ == "__main__":
    transactions: List[str] = deserialize("List[str]", read_line())
    ans = Solution().invalidTransactions(transactions)
    print("\noutput:", serialize(ans, "string[]"))
