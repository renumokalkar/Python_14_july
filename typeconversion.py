#integer to string,float and bool
num=123
print(type(num),num)
a=str(num)
print(type(a),a)
b=float(num)
print(type(b),b)
c=bool(num)
# print(type(c),c)

#string to bool
st="abc"
print(type(st),st)
d=bool(st)
print(type(d),d)

#float to integer,string,bool
flo=12.45
print(type(flo),flo)
e=int(flo)
print(type(e),e)
f=str(flo)
print(type(f),f)
g=bool(flo)
print(type(g),g)

#bool to string,integer,float
h=bool(1)
print(type(h),h)
i=str(h)
print(type(i),i)
j=int(h)
print(type(j),j)
k=float(h)
print(type(k),k)
