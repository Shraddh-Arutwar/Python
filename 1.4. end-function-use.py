"""
if i/p: n=3
o/p: 123

n=5
o/p: 12345
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')
