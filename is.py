set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

intersection = [i for i in set_a.intersection(set_b)]

intersection.sort()
print(*intersection)
