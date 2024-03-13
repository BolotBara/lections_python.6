"""
1. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""

class MyList(list):
    def __getitem__(self, index):
        if isinstance(index, int):
            _index = index - 1
            return super().__getitem__(_index)
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if isinstance(index, int):
            _index = index - 1
            super().__setitem__(_index, value)
        else:
            super().__setitem__(index, value)

x = MyList([1, 2, 3, 4, 5])
print(x[1]) 

# Мы создаём класс MyList, который наследуется от встроенного класса list.
# В методе __getitem__ мы переопределяем поведение получения элемента по индексу. Если индекс, переданный в метод __getitem__, является целым числом, мы вычитаем 1 из этого индекса, чтобы сделать индексацию, начиная с 1, а затем вызываем метод __getitem__ базового класса list с скорректированным индексом. Это позволяет нам получать элементы списка, начиная с индекса 1.
# Аналогично, в методе __setitem__ мы переопределяем поведение установки элемента по индексу. Если индекс является целым числом, мы также корректируем индекс на 1 и вызываем метод __setitem__ базового класса list с этим скорректированным индексом.
# В примере использования мы создаём экземпляр x класса MyList, передавая в него список [1, 2, 3, 4, 5]. Затем мы обращаемся к элементу с индексом 1, и он возвращает значение 1, так как индексация начинается с 1.


"""
2. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе new напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""

class Word(str):
    def __new__(cls, obj):
        obj = obj.replace(' ', '')
        return super().__new__(cls, obj)

    def __init__(self, obj) -> None:
        super().__init__()
        self.obj = obj

    def __gt__(self, other):
        print('gt worked')
        print(self, '---', other)
        if len(self) > len(other):
            return self
        elif len(self) < len(other):
            return other
        else:
            return 'eq'
        
    def __it__(self, other) -> bool:
        return len(self) < len(other)
    
    def __eq__(self, other) -> bool:
        return len(self) == len(other)

obj = Word('           Hello John    ')
obj2 = Word(' God i  fy')

print(obj > obj2)
print(obj < obj2)
print(obj == obj2)




"""
3. Создайте класс BankAccount, представляющий банковский счет. Реализуйте магические методы init, str, add и sub, чтобы поддерживать инициализацию счета, вывод информации о счете и операции пополнения и снятия средств.
"""








