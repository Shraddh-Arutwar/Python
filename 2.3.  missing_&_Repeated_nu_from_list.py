# Find missing elements from list
# Find the numbers of times number repeated in list

a = [1, 5, 9, 10, 7, 4, 10, 5, 6, 10]
b = []

for i in range(1,11):
    for j in range(0,int(len(a))):
        if a[j]==i:
            break
    else:
      b.append(i)

print("missing elements from list are: ", b)

visited = [False for i in range(len(a))]
for i in range(len(a)):
    if (visited[i] == True):
        continue
    count = 1
    for j in range(i + 1, len(a)):
        if (a[i] == a[j]):
            visited[j] = True
            count += 1

    if (count!=1):
        print(a[i], "repeated", count, "times",end=' | ')


