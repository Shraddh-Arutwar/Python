s1 = input("Enter a string: ")

# siplest using reverting string
if s1 == s1[::-1]:
    print("{0} string is palindrome".format(s1))
else:
    print("{0} string is not palindrome".format(s1))

# by not using reverse string
for i in range(0, int(len(s1)/2)):
    if s1[i] != s1[len(s1)-i-1]:
        print("{0} is not palindrome".format(s1))
        break
else:
    print("{0} is palindrome".format(s1))
