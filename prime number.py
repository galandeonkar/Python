n=int(input("Enter num :"))

result=0

if n==0 or n==1:
    result=1

    for i in range(2,n):
        if n%i==0:
            result=1

            if result==1:
                print("Number is not Prime number.")

                else:
                    print("Number is prime number.")
            
        
