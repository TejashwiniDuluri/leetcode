from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gas_level = 0
        start_station = 0
        total_have = 0
        total_required = 0

        for station, gas_we_have in enumerate(gas):
            total_required += gas_we_have
            total_have += cost[station]
                     
            curr_gas_level = curr_gas_level + gas_we_have - cost[station]
            print("curr_gas_level:",  curr_gas_level, "gas_we_have:" , gas_we_have, "=======")
            if curr_gas_level < 0: # break the chain that means we do not have suff gas to reach next station                
                start_station = station+ 1
                curr_gas_level = 0

        if total_required < total_have :
            return -1   
        return start_station
            

gas = [1,2,3,4,5] #=> what amount of gas we have at these stations
cost = [3,4,5,1,2] #=> what amount of gas we require to reach next station  
# gas = [2,3,4]
# cost = [3,4,3]
gas =[5,1,2,3,4]
cost =[4,4,1,5,1]
obj = Solution()
print(obj.canCompleteCircuit(gas, cost))
        
# always what we have and what we required should be gas >= cost 
# 1 => start from 1 => 1-3 = -2
# 2 => start from 2 => 2-4 = -2
# 3 => start from 3 => 3-5 => -2
# 4 => start from 4 => 4-1 => 3
# 5 => start from 5 => 5-2 => 3