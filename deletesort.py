list = []
n=int(input("Enter the no of elements  "))
for i in range(0,n):
    n1 = int(input())
    list.append(n1)
list.sort()
l2 =list((set(list)))
print(l2)