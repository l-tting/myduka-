class Test1:
    def sum_numbers(self):
        return 4 + 5

class Test2(Test1):
    def sum_numbers(self,x,y):
        return x + y

class Test3(Test1):
    def sum_numbers(self,x,y,z):
        return x + y + z


test1 = Test3()
sum1 =test1.sum_numbers(2,3,4)
print(sum1)