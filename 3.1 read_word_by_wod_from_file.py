
# Print words in file
with open("abc.txt") as f:
   for line in f:
       for word in line.split():
           print(word, end='|')

# Print characters in file
with open("abc.txt","r") as f:
   f.seek(0)
   while True:
       char = f.read(1)
       if not char:
           break
       print(char,end = '|')
