n=int(input())
l=[0 for x in range(n)]
nq=int(input())
while nq > 0 :
     # q=[int(x) for x in str(input()).split(1)]
     q = [[int(input("Enter single number: ")) for _ in range(n)] for _ in range(n)]
     for i in range(q[0]-1,q[0]):
            l[i]=l[i]+q[2]
l.sort()
print(l[n-1])
'''list = [[1,5,3],[4,8,7],[6,9,1]]
l=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,4):
    f1=list[i][0]
    f2=list[i][1]
    f3=list[i][2]
    for j in range(f1,f2+1):
            l[j]=l[j]+f2
l.sort()
print(l[9])
        
n=int(input("Enter the size of list: "))
quer = [[int(input("Enter single number: ")) for _ in range(n)] for _ in range(n)]
li=[0,0,0,0,0,0,0,0,0,0]
for i in range(3):
    for j in range(quer[i][0],quer[i][1]+1):
        li[j-1]=li[j-1]+quer[i][2]
    print(li)
li.sort()
print(li[9])'''