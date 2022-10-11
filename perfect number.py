n=int(input("Enter a num:"))

result=0

for i in range(1,n):
    if n%i==0:
        result += i

if n==result:
    print("Number is perfect.")
else:
    print("Number is not perfect.")
