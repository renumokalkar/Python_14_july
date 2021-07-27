print("THIS IS TASK 1")
s="this is python cookbook Python is open source java is robust programming language hello world i like learning python"
l=list(s.split(" "))
max_len=0
for i in l:
    if len(i)>max_len:
        max_len=len(i)
        res=i
print(res)


print("\nTHIS IS TASK 2")
s1="this is python cookbook\nPython is open source\njava is robust programming language\nhey world\ni like learning python"
l1=s1.split('\n')
for i in l1:
    for j in i:
        s2=i.split(" ")
    print(s2)
    print("THIS IS A LONGEST STRING:",max(s2,key=len))


