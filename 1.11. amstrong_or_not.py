"""
Amstrong no: 153
i.e. 1^3 + 5^3 + 3^3 = 153
"""
num = int(input("enter a no: "))
temp = num
sum = 0

while num > 0:
    dig = num % 10
    sum = sum + dig**3
    num = num//10

if sum == temp:
    print("Amstrong")
else:
    print("Not Amstrong")
