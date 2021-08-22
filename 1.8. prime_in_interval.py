si = int(input("Start interval: "))
ei = int(input("End Interval: "))

for i in range(si, ei+1):
    int(i)
    if i==0:
        print("No valid entery")
    else:
        for x in range(2, i//2):
            if (i%x==0):
                break
        else:
            print(i)

