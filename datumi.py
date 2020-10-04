datums="10/12/10"
dat= list(datums.split("/"))
print("1.gadijums ",dat)
isais=[4,6,9,11]
garais=[1,3,5,7,8,10,12]
varianti=[]
def gg(x):
    if x%4==0:
        dd=29
    else:
        dd=28
    return dd

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

if dat[0]==dat[1]==dat[2]:
    varianti.append(1)
else:
    parb(int(dat[0]),int(dat[1]),int(dat[2]))
    print(varianti)
    dat[0],dat[1]=dat[1],dat[0]
    print("2.gadijums ",dat)
    parb(int(dat[0]),int(dat[1]),int(dat[2]))
    dat[1],dat[2]=dat[2],dat[1]
    print("3.gadijums ",dat)
    parb(int(dat[0]),int(dat[1]),int(dat[2]))
    dat[0],dat[1]=dat[1],dat[0]
    print("4.gadijums ",dat)
    parb(int(dat[0]),int(dat[1]),int(dat[2]))
    dat[2],dat[1]=dat[1],dat[2]
    print("5.gadijums ",dat)
    parb(int(dat[0]),int(dat[1]),int(dat[2]))
    dat[0],dat[1]=dat[1],dat[0]
    print("6.gadijums ",dat)
    parb(int(dat[0]),int(dat[1]),int(dat[2]))
    print(varianti)

atbilde=sum(varianti)
print(f"Iespējami ir {atbilde} varianti")





