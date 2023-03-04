#Find the longest substring with k unique characters in a given string
str=input("Enter the string : ")
def count(str):
    s = set(str)
    return len(s)
k=int(input("Enter the value of K :  "))
l=len(str)
lii=[]
s1=[]
li = [str[i: j] for i in range(len(str))
          for j in range(i + 1, len(str) + 1)]
#li.sort()
print(li)

for i in range (len(li)):
    lii.append(count(li[i]))
print(lii)   
for i in range(len(lii)):
    if lii[i]==k:
        s1.append(len(li[i]))
print(max(s1))


