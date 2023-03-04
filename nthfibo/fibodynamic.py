def fibo(n):
    n1=0
    n2=1
    if n==1:
        return(1)
    elif n==0:
        return(0)
    elif n>1:
        for i in range(2,n):
            n3=n1+n2
            n1=n2
            n2=n3
        return(n2)



n=int(input("Enter the no  :  "))
print(fibo(n))
