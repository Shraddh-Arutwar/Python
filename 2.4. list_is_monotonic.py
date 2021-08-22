# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

def isMonotonic(a):
    if (all(a[i] <= a[i+1] for i in range(len(a)-1))):
        print("incrising Monotonic")
    if (all(a[i] >= a[i+1] for i in range(len(a)-1))):
        print("decreasing Monotonic")

n = int(input("Enter numbers in list: "))
a = []
for i in range(n):
    num=int(input("Enter no: "))
    a.append(num)

print(a)

isMonotonic(a)