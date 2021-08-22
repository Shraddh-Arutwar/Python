# use *range() --> for unpacking the range function output

a= [*range(1,11)]

# Array Rotation
b = []
for i in range(0, len(a)):
    n = a[len(a)-i-1]
    b.append(n)
print("reverse list is: ", b)

# OR for reversing list
print("Reverse the list a without using another list: ",end=' ')
print(a[::-1])

# array rotation by index 3
r_index=int(input("Rotate list by index: "))
b = []

for i in range(r_index, len(a)):
    n = a[i]
    b.append(n)

for i in range(0,r_index):
    n = a[i]
    b.append(n)

print("rotate array by index by", r_index ,": " ,b)