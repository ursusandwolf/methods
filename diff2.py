set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

diff = [i for i in set_a.difference(set_b)]

diff.sort()
print(*diff)
