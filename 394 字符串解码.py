题解： 用栈去做,记录multi的res
class Solution:
    def decodeString(self, s: str) -> str:
        stack,res,multi=[],"",0
        for c in s:
            if c=="[":
                stack.append([multi,res])
                multi,res=0,""
            elif c=="]":
                multi,latest_res=stack.pop()
                res=latest_res+multi*res
            elif "0"<=c<="9":
                multi=multi*10 + int(c)
            else:
                res=res+c
        return res

      
