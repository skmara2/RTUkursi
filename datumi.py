datums="2/29/99"
dat= list(datums.split("/"))
print("1.gadijums ",dat)
isais=[4,6,9,11]
garais=[1,3,5,7,8,10,12]
varianti=[]

def gg(x):
    if x%4==0:
        dienas=29
    else:
        dienas=28
    return dienas

def parb(a,b,c):
    if a in isais and b<=30:
        varianti.append(1)
        print("1 ",varianti)
    elif a in garais and b<=31:
        varianti.append(1)
        print("2 ",varianti)
    else: 
        d=gg(c)
        if a==2 and b<=d:
            varianti.append(1)
            print("3 ",varianti)
    return varianti

if int(dat[0])==int(dat[1])==int(dat[2])<=12:
    varianti.append(1)
else:
    a=int(dat[0])
    b=int(dat[1])
    c=int(dat[2])

    parb(a,b,c)
    print(varianti)
    if a!=b:
        print("2.gadijums ",b,a,c)
        parb(b,a,c)
    print("3.gadijums ",c,b,a)
    parb(c,b,a)
    if c!=b:
        print("4.gadijums ",b,c,a)
        parb(b,c,a)
    print("5.gadijums ",a,c,b)
    parb(a,c,b)
    if a!=c:
        print("6.gadijums ",c,a,b)
        parb(c,a,b)
    print(varianti)

atbilde=sum(varianti)
print(f"Iespējami ir {atbilde} varianti")





