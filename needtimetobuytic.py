class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0
        i = 0

        # while tickets[k] != 0:

        while tickets[k] > 0:
            if tickets[i] != 0:
                tickets[i] -=1
                sec +=1

            i = (i+1) % len(tickets)

        return sec
         


# Input: tickets = [2,3,2], k = 2
# Output: 6

# Input: tickets = [5,1,1,1], k = 0
# Output: 8