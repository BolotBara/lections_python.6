# Напишите класс Subscriber, у которого есть переменные экземпляра:
# firstname
# lastname
# Сделайте так, чтобы метод __repr__ возвращал firstname + lastname
# Напишите класс Provider, у которого есть:
# переменный экземпляра name -- название провайдера
# переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
# переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber, значением является сумма (вещественное число)
# метод register_payment, который принимает экземпляр класса Subscriber, и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
# Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
# Если нет, выкидывает (raise) ошибку ValueError
# Напишите класс Terminal, у которого есть:
# переменная экземпляра amount = 0
# переменная экземпляра providers = [ ]
# Регистрировать провайдера через метод register, который принимает экземпляр класса Provider и добавляет в providers
# Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider, экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться метод register_payment экземпляра класса Provider. register_payment успешно сработал, то в переменую amount нужно добавить сумму.


# class Subscriber:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def __repr__(self):
#         return f'{self.firstname} {self.lastname}'
    
# class Provider:
#     def __init__(self,name) -> None:
#         self.name = name
#         self.subscribers = []
#         self.payments = {}

#     def register_payment(self, Subscriber, amount):
#         if Subscriber in self.subscribers:
#             self.payments[Subscriber] = amount
#         else:
#             raise ValueError('Экземпляр не найден')

#     def ed_Subscriber(self, Subscriber):
#         self.subscribers.append(Subscriber)

# class Terminal:
#     def __init__(self) -> None: 
#         self.amount = 0
#         self.providers = [ ]

#     def register(self, Provider):
#         self.providers.append(Provider)

#     def pay(self,Provider, Subscriber, amount):
#         Provider.register_payment(Subscriber,amount )
#         self.amount += amount

# subscriber1 = Subscriber('Тима', 'Анвар')
# subscriber2 = Subscriber('Анарбек', 'Санжар')

# provider = Provider('Наш провайдер')

# provider.ed_Subscriber(subscriber1)
# provider.ed_Subscriber(subscriber2)

# terminal = Terminal()

# terminal.register(provider)

# try:
#     terminal.pay(provider, subscriber1, 100.0)
#     terminal.pay(provider, subscriber2, 150.0)
# except ValueError as e:
#     print(e)

# print('Собранно:', terminal.amount)
