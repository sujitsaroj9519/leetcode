class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c = coordinates
        if c[0] =='a' or c[0]=='c' or c[0]=='e' or c[0]=='g':
            if int(c[1])%2==0:
                return True
            else:
                return False

        else:
            if int(c[1])%2==0:
                return False
            else:
                return True
        
obj= Solution()
print(obj.squareIsWhite("a2"))