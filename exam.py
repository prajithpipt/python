ss="qburst"
l=len(ss)
for i in range(0,l):
    for j in range(0,i+1):
        print(ss[j],end=" ")
    print("")
for i in range(l,0,-1):
    for j in range(0,i-1):
        print(ss[j],end=" ")
    print("")
ll=2*l-2
for i in range(0,l):
    for j in range(0,ll):
        print(end=" ")
    ll=ll-2
    for j in range(0,i+1):
        print(ss[j],end=" ")
    print("\r")
"""
for i in range (l,0,-1):
    for j in range(0,i):
        print(j, end="")
        j=j+j
    print("")"""