a = float(input ("a = "))
b = 10
c = -10
d = 6
e = -6
f = 24
g = -24
if f > a > b:
    print(" Ans: " + str(a//2))
if b > a > d:
    print(" Ans: " + str(a**2))
if e > a > c:
    print(" Ans: " + str(a / e))
if a > f:
    print(" Ans: " + str(a*f))
if g > a:
    print(" Ans: " + str(a+g)) 
if c > a > g:
    print(" Ans: " + str(a-g))
else:
    print(" 0 ")
