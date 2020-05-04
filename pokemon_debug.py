import random

class Test:
    def __init__(self, num, lists):
        self.num = num
        self.lists = lists

lst = []
for num in range(0,5):
    lst.append(str(num) + "ayyyy")

print(lst)
ran_num = random.randint(1,5)

test_instance = Test(ran_num, lst)

class Internal:
    def __init__(self, thing):
        self.thing = thing

    def call(self):
        print (self.thing.num)
        print (self.thing.lists[self.thing.num - 1])


test_internal = Internal(test_instance)
test_internal.call()
