
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


    def talks(self,words):
        print(f"{self.name} talks and said {words}")


    def sleeps(self,time):
        print(f"{self.name} sleeps at {time}")


    def display_info(self):
        print("-------Object Info-----------")
        print(f'Name : {self.name}')
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")



# person1 object
person1 = Person("Alice Kamau",23,"Female")
print(type(person1))
person1.display_info()
person1.talks("OOP is very easy")
person1.sleeps("10pm")

print("--------------------------------------------")


#person2 object
person2 = Person("Jack", 25, "Male")
print(type(person2))
person2.display_info()
person2.talks("Python is just too hard")
person2.sleeps("11pm")



