print("THIS IS TASK 1")
num=[1,2,5,4,10,5]
num1=[]
num2=[]
for i in num:
    if i%2==0:
        num1.append(i*50)
print("num1" ,num1,end='')
for i in num:
    if i%2!=0:
        num2.append(i*50)
print("\nnum2",num2,end='')
print('\n')



print("\nTHIS IS TASK 2")
l1=[234,556,233,454,1221,3243]
l2=list(map(str,l1))
for i in l2:
    if i==i[::-1]:
        print((f"{i} is palindrome"))
    else:
        print(f"{i} is not palindrome")


print("\nTHIS IS TASK 3")
l1=[2,4,5,6,7,1,5,9,2,2,5]
duplicate=[]
unique=[]
for num in l1:
    a=l1.count(num)
    if a>1:
        for i in range(a):
            l1.remove(num)
        duplicate.append(num)

for num in l1:
    if a==1:
        unique.append(num)

print("duplicate",duplicate)
print("unique=",unique)






