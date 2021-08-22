# use *range() --> for unpacking the range function output

a = [*range(1,11)]
sum = 0

print("list is: ", a)
for x in range(0, len(a)):
    sum = sum + int(a[x])

print("sum of array no: ", sum)

# Largest number in arrays
n = 0
for i in range(0, len(a)):
    if a[i] > n:
        n = a[i]
print ("largest number is:", n)