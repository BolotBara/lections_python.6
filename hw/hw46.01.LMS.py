# Задача 1: "Dollar"
# Цель: Создать функцию dollarize, преобразующую числа в долларовый формат, и класс MoneyFmt для управления денежными суммами.
# Описание:
# Функция dollarize должна принимать дробное число и возвращать строку, представляющую сумму в долларовом формате.
# Класс MoneyFmt использует внутренний атрибут amount для хранения денежной суммы и предоставляет методы для обновления суммы, возвращения ее как строки в долларовом формате и как исходного числового значения.
# Пример использования:
# cash = MoneyFmt(12345678.021) 
# print(cash) -- выводит "$12,345,678.02" 
# cash.update(100000.4567) 
# print(cash) -- выводит "$100,000.46" 
# cash.update(-0.3) 
# print(cash) -- выводит "-$0.30" 
# repr(cash) -- выводит -0.3 

# def dollarize(number):
#     return "${:,.2f}".format(number)

# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount

#     def update(self, new_amount):
#         self.amount = new_amount

#     def __str__(self):
#         return "${:,.2f}".format(self.amount)

#     def __repr__(self):
#         return str(self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)  
# cash.update(100000.4567)
# print(cash)  
# cash.update(-0.3)
# print(cash) 


# Задача 2: "Велосипед"
# Цель: Реализовать класс Bike, моделирующий велосипед с различными атрибутами и методами управления.
# Описание:
# Класс должен содержать атрибуты для стоимости, производителя, модели, года выпуска, состояния, цены продажи и статуса продажи.
# Методы должны позволять устанавливать цену продажи, учитывая минимальную прибыль, обслуживать велосипед, изменяя его состояние и стоимость ремонта, и продавать велосипед, изменяя его статус и рассчитывая прибыль.

# class Bike:
#     def __init__(self, price, manufacturer, model, year, condition, sale_status):
#         self.price = price
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self.sale_status = sale_status
#         self.minimum_profit = 50 

#     def set_sale_price(self, sale_price):
#         if sale_price > self.price + self.minimum_profit:
#             self.sale_price = sale_price
#         else:
#             print('Цена продажи слишком низкая.')

#     def service_bike(self, cost_of_service):
#         self.condition += 10
#         self.price += cost_of_service

#     def sell_bike(self):
#         if self.sale_status == 'Ready_for_sale':
#             self.sale_status = 'Sold'
#             profit = self.sale_price - (self.price + self.minimum_profit)
#             print(f'Велосипед продан! Прибыль составила {profit}$.')
#         else:
#             print('Велосипед уже продан.')

# bike = Bike(1, 'Liberty', 'Sky', '2024', 2, 'Ready_for_sale')
# bike.set_sale_price(200)
# bike.service_bike(20)
# bike.sell_bike()



# Задача 3: "Герой"
# Цель: Разработать программу, имитирующую взаимодействие между солдатами и героями в контексте игры-стратегии.
# Описание:
# Необходимо создать классы для солдат и героев, каждый с уникальным номером и принадлежностью к команде.
# Солдаты могут "следовать" за героями своей команды, а герои могут повышать свой уровень.
# В программе должны генерироваться солдаты для двух команд, после чего сравнивается количество солдат в каждой команде, и у героя команды с большим числом солдат повышается уровень.

# class Hero:
#     def __init__(self,team) -> None:
#         self.team = team
#         self.level = 1

#     def level_up(self):
#         self.level += 1

#     def follow(self, soldiers):
#         while len(soldiers) > 10:  
#             self.level_up() 
#             soldiers.pop() 

# class Soldier:
#     def __init__(self, num, team):
#         self.num = num
#         self.team = team

# soldiers_team_a = [Soldier(i, 'a') for i in range(20)]
# soldiers_team_b = [Soldier(i, 'b') for i in range(25)]

# hero_team_a = Hero('a')
# hero_team_b = Hero('b')

# hero_team_a.follow(soldiers_team_a)
# hero_team_b.follow(soldiers_team_b)

# while len(soldiers_team_a) > len(soldiers_team_b):
#     hero_team_a.level_up()

# while len(soldiers_team_a) < len(soldiers_team_b):
#     hero_team_b.level_up()

# print(f'Уровень героя команды A: {hero_team_a.level}')
# print(f'Уровень героя команды B: {hero_team_b.level}')


