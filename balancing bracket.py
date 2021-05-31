'''def Balancing(S):
    l = []
    for i in S:
        if i == '{' or i == '(' or i == '[':
            l.append(i) # push
        elif i == '}' or i == ')' or i == ']':
            if len(l) == 0:
                return False
            top_element = l.pop() 
            if not check(top_element, i):
                return False
    if len(l) != 0:
        return False       
    return True 
def check(start, end):
    if start == '(' and end == ')':
        return True
    if start == '[' and end == ']':
        return True
    if start == '{' and end == '}':
        return True  
    print('invalid')
print(Balancing("{ABC(AE[KH])}"))

'''
x = ['ab', 'cd']
print(len(list(map(list, x))))
'''
import re
l = ["hello (you)", "hi(how are you)", "welcome (to class)"]
for i in l:
    print(re.sub(r" ?\([^)]+\)", "", i))

class balancing:
   def valid(self, s):
        l, p = [], {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in p:
                l.append(i)
            elif len(l) == 0 or p[l.pop()] != i:
                return False
        return len(l) == 0

print(balancing().valid("(){}[]"))
'''
class validity:
    def f(str):
        a= ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str
s = input("enter : ")
print(s, "-", "is Valid"
      if validity.f(s) else "is Invalid")

