思路：
用栈算

s=input().strip()
stack=[]
for char in s:
    if char=="]":
        temp=[]
        while stack[-1]!="[":
            temp.append(stack.pop())
        stack.pop()
        count,childS="".join(temp[::-1]).split("|")
        childS=int(count)*childS
        for i in childS:
            stack.append(i)
    else:
        stack.append(char)
print("".join(stack))
