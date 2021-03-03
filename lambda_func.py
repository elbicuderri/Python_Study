s = [[2, 3, 1], [3, 4, 3], [4, 5, 2]]
[x, y, z] = min(s, key = lambda t: t[2])

print([x, y, z])

L1 = list(range(11))

L2 = list(filter(lambda s: s%2 == 1, L1))

L22 = [ x for x in range(11) if x%2 == 1 ]

print(L2)

print(L22)

L3 = list(map(lambda s: s*2, L1))

L33 = [ x*2 for x in range(11)]

print(L3)

print(L33)