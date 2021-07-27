l=[11,2,55,890,45,98]
max_no=l[0]
min_no=l[0]
for i in range(1,len(l)):
    if l[i]<min_no:
        min_no=l[i]
    if l[i]>max_no:
        max_no=l[i]
print("MAXIMUM NUMBER FROM {} IS {}".format(l,max_no))
print("MINIMUM NUMBER FROM {l} IS {min_no}")
