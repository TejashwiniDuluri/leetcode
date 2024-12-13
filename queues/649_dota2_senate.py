
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        n = len(senate)

        for ind, i in enumerate(senate):
            
            if i == "D":
                dire.append(ind)
            else:
                radiant.append(ind)
        
        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.pop(0)
                radiant.append(radiant[0] + n)
                radiant.pop(0)

            else:
                radiant.pop(0)
                dire.append(dire[0] + n)
                dire.pop(0)

        
        return "Radiant" if radiant else "Dire" 

obj=Solution()
senate = "RDD"
# senate = "RD"
print(obj.predictPartyVictory(senate))
        
