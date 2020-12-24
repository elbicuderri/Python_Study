# Python_Study

```python
# iterator란
a_iter = (a for a in range(10))

for i in range(10):
    print(next(a_iter))
```

```python
# python 문자열
a = 'abcd'
b = a[::-1] # 문자열 뒤집기

c = ['a', 'b', 'c', 'd']
d = ''.join(c) # list 문자열로 합치기
```


```python
# list 중 두 수의 차(절대값)가 적은 경우의 수(들)을 찾는 방법
import itertools

target = [1, 4, 5, 6, 7, 2, 3, 4, 3, 4, 2, 3, 4, 5 ,-1, 3]

c = list(itertools.combinations(target, 2))

ee = [ abs(e[0]-e[1]) for e in c]

m_indexes = ee.index(max(ee)) 
```
