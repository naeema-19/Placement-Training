n=int(input("Enter a no :"))
p=n
s=0
while(n>0):
    num=n%10
    s=(s*10)+num
    n=n//10
if(s==p):
    print("Palindrome")
else:
    print("Not")



