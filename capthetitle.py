class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split(' ')
        s = []

        for w in l:
            if len(w) >2:
                s.append(w.capitalize())
            else:
                s.append(w.lower())
        return ' '.join(s)

       


# Input: title = "i lOve leetcode"
# Output: "i Love Leetcode"

# Input: title = "First leTTeR of EACH Word"
# Output: "First Letter of Each Word"

# Input: title = "capiTalIze tHe titLe"
# Output: "Capitalize The Title"