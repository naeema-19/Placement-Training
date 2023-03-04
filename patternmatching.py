s=input("Enter the string combination :")
f=0
k=0
for i in range(len(s)):
    if s[i]=='{':
        f=f+1
    elif s[i]=='}':
        f=f-1
    if f<0:
        k=1
        break;
print(f)
if k==0 and f==0:
    print("matching")
else:
    print("not matching")

