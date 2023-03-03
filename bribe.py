b=0
n=int(input("Enter the length of the queue : "))
q = []
k=0
for i in range(0, n):
    n1 = int(input())
    q.append(n1) 
for i in range(0,n):
    f=q[i]-(i+1)
    if f>2:
        print("Too Chaotic")
    elif f>0:
        print(f)
        
        


