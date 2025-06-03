class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    def prnt(self):
        return self.__stack_list


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack() # Stack den türetilmişif sınıf
stack_object2 = Stack() # Ana sınıf

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    stack_object2.push(stack_object.pop())


print(stack_object2.prnt()) 
    
