n = input()
s = set([c for c in n])

for c in n:
    if c in s:
        print(c,end='')
        s.remove(c)
