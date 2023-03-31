n = [c for c in input() if c.isdigit()]
previous = 0
s = set()
result = set()

for d in n:
    s.add(d)
    if len(s) == previous:
        result.add(d)
    previous = len(s)

p = list(result)
p.sort()
print(*p if len(p)>0 else ["NO"])
