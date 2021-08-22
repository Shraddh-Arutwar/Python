# take index from user which they want to swap and return the swaped list

def swapList(a,n,m):
    a[n], a[m] = a[m], a[n]
    return(a)

def length(a):
    count = 0
    for i in a:
        count = count+1
    return(print(count))

a = [*range(0,11)]
n = int(input("swap from: "))
m = int(input("swap to: "))
swapList(a,n,m)
print(a)
length(a)
