# self의 이해
class SelfTest():
    def function1():
        print('function1 called!')
    def function2(self):
        #print(id(self))
        print('function2 called!')        

self_test = SelfTest()
# self_test.function1()
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)