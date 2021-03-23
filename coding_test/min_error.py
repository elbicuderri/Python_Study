import itertools

target = [1, 4, 5, 6, 7, 2, 3, 4, 3, 4, 2, 3, 4, 5 ,-1, 3]

c = list(itertools.combinations(target, 2))

ee = [ abs(e[0]-e[1]) for e in c]

m_idx = ee.index(max(ee)) ## point

print(c[ee.index(max(ee))])