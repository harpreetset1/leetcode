
class Solution:
    def reverse(self, x: int) -> int:
        import math
        if(math.pow(-2,31) > x or x > math.pow(2,31) - 1):
            return 0
        str_int = x
        neg = ""
        if(x<0):
            str_int = str(x)[1:]
            neg = "-"
        else:
            str_int = str(x)
        str_int = str_int[::-1]
        if(math.pow(-2,31) > int(neg+str_int) or int(neg+str_int) > math.pow(2,31) - 1):
            return 0
        else:
            return int(neg+str_int)

s = Solution()        
print(s.reverse(15336469))

