st="python programming hello world"
for i in range(len(st)):
    end_v="-"
    if i==len(st)-1:
        end_v=''
    elif st[i]==" ":
        continue
    elif st[i+1]==" ":
        end_v="\n"
    print(st[i],end=end_v)



