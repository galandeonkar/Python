n=int(input("Enter no of rows:"))

for i in range(n):
    val=i+1
    dec=n-1
    for j in range(i+1):
        print(val,end=" ")
        val=val+dec
    print()
