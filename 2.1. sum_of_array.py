a = [1, 20, 10, 50, 10]
sum = 0

for x in range(0, len(a)):
    sum = sum + int(a[x])

print("sum of array no: ", sum)

# Largest number in array
n = 0
for i in range(0, len(a)):
    if a[i] > n:
        n = a[i]
print ("largest number is:", n)

# Array Rotation
b = []
for i in range(0, len(a)):
    n = a.pop()
    b.append(n)
print(b)
