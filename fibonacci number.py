import math
def perfectsquare(x):
    s=int(math.sqrt(x))
    return s*s==x
    
n=int(input("Enter a num: "))

result1 = 5*(n*n)+4
result2 = 5*(n*n)-4

if perfectsquare(result1) or perfectsquare(result2):
    print(n," is fibonacci number")
else:
    print(n," is not a fibonacci number")
