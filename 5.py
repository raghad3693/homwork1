even_num=[]
x=int(input("Enter the decimai number :"))
y=x
while y != 0 :
    z=y%2
    even_num.append(z)
    y=y//2
even_num.reverse()
w=" "
for i  in even_num:
    w=w +str(1)
print(w)