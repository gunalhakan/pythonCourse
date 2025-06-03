class Stack:
    # self parametresi kullanılmasa bile tüm fonksiyonlarda olmak zorundadır
    # fonksiyonlar arasında değer aktarımı self üzerinden yapılır.
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

stack1.push(1) # stack1 e 1 ekle
stack2.push(stack1.pop() + 1) # stack1 den son sayıyı(1) sil, sildiğin sayıya 1 ekle(2), stack2 ye ekle
stack3.push(stack2.pop() - 2) # stack2 den son sayıyı(2) sil, sildiğin sayıdan 2 çıkart(0), stack3 e ekle

print(stack3.pop()) # stack3 e eklediğin son sayıyı sil
