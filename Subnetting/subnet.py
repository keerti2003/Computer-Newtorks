import math

def calbit(nh,bitl):
    #bitl = []
    for i in range(0,len(nh)):
        for j in range (2,8):
            if math.pow(2,j) > nh[i] :
                bitl.append(j)
                break
    
def mask(bitl,addr):
    c = 25
    stadd = []
    addr1 = addr.split('.')
    x = addr1[len(addr1)-1]
    y = int(x)
    #print("Slash notation for subnet 1 is ",c)
    print("Address of subnet 1 is ",addr,"/",c)
    
    for i in range(0,len(bitl)-1):
        c = c+1
        #print("Slash notation for subnet ",i+2," is ",c)
        y = y + math.pow(2,bitl[i])
        s = str(y)
        addr1[len(addr1)-1] = s
        z = ''
        for j in range (len(addr1)):
            if j!=len(addr1)-1:
                z = z + addr1[j]+ '.'
            else:
                z = z + addr1[j]
        print("Address of subnet ",i+2," is ",z,"/",c)

addr = input("Enter the starting address: ")
ns = int(input("Enter number of subnets: ")) #no. of subnets
nh = []
bitl = []

for i in range(ns):
    h = int(input("Enter hosts: "))
    nh.append(h)
calbit(nh,bitl)
mask(bitl,addr)
