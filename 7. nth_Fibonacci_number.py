n = int(input("Enter nth Position: "))
a = 0
b = 1
list1 = [0,1]

if n<0:
    print("not valid")
elif n==0:
    print(0)
elif n==1:
    print(1)
else:
    for x in range(2, n):
        c = a + b
        a = b
        b = c
        list1.append(b)

    print(b)
    print(list1)
