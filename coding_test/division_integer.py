# 각 자리의 수로 나누어 떨어지는 모든 두 자리 양의 정수들의 합을 구하여라. 

sum = 0
for n in range(10, 100):
    p = n / 10
    q = n % 10
    if (q == 0):
        continue
    if (n % p == 0 and n % q == 0):
        sum += n
        
print(sum)