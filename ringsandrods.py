class Solution:
    def countPoints(self, rings: str) -> int:

        c= 0
        for i in range(10):
            i = str(i)
            if "R"+i in rings and "G"+i in rings and "B"+i in rings:
                c+=1
        return c 


# Input: rings = "G4"
# Output: 0

# Input: rings = "B0R0G0R9R0B0G0"
# Output: 1

# Input: rings = "B0B6G0R6R0R6G9"
# Output: 1