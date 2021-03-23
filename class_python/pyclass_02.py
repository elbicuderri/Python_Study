# 예제3 # 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1 
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) #클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) 
print(user2.stock_num) 
print(user3.stock_num) 
# 자기 네임스페이스에 없으면 
# 클래스의 네임스페이스에 가서 변수를 찾고,
# 거기에도 없으면 에러가 발생한다.

del user1

print(user2.stock_num)
print(user3.stock_num)