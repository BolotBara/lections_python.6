# Задание: Работа с базой данных PostgreSQL
# Цели задания:
# Проверка знаний и умений по добавлению, обновлению и заполнению данными таблиц в базе данных PostgreSQL.
# Описание задания:
# В рамках данного задания вам предстоит работать с базой данных для интернет-магазина. Вам будет необходимо создать таблицы, добавить в них данные, обновить определенные записи и выполнить ряд запросов для проверки введенной информации.

# Часть 1: Подготовка базы данных

# 1. Создайте базу данных OnlineStore`.
# CREATE DATABASE OnlineStore;

# 2. Внутри базы данных создайте следующие таблицы:

# Products (Товары): id (первичный ключ), name (имя), price (цена), quantity (количество на складе).

# CREATE TABLE Products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     price DECIMAL(10, 2),
#     quantity INT
# );

# Customers (Покупатели): id (первичный ключ), first_name (имя), last_name (фамилия), email (электронная почта).

# CREATE TABLE Customers (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(100),
#     last_name VARCHAR(100),
#     email VARCHAR(250)
# );

# Orders (Заказы): id (первичный ключ), customer_id (внешний ключ к таблице Customers), order_date (дата заказа), total_amount (общая сумма).

# CREATE TABLE Orders (
#     id SERIAL PRIMARY KEY,
#     customer_id INT REFERENCES Customers(id),
#     order_date DATE,
#     total_amount DECIMAL(10, 2));

# Часть 2: Заполнение таблиц данными

# 1. Добавьте не менее пяти записей в таблицу 'Products'.

# INSERT INTO Products (name, price, quantity) 
# VALUES 
#     ('Product 1', 10.10, 10),
#     ('Product 2', 11.11, 11),
#     ('Product 3', 12.12, 12),
#     ('Product 4', 13.13, 13),
#     ('Product 5', 14.14, 14);

# 2. Добавьте не менее трех записей в таблицу Customers.

# INSERT INTO Customers (first_name, last_name, email) 
# VALUES 
#     ('Anarbek', 'Chimberdiev', 'chimberdiev@gmail.com'),
#     ('Bolot', 'Kozhomberdiev', 'kozhomberdiev@gmail.com'),
#     ('Diana', 'Talaibekova', 'talaibekova@gmail.com');

# 3. Создайте заказы в таблице Orders, связав их с покупателями и укажите общую сумму заказа.

# INSERT INTO Orders (customer_id, order_date, total_amount) 
# VALUES 
#     (1, '2024-03-12', 25.10),
#     (2, '2024-03-11', 35.10),
#     (3, '2024-03-10', 45.10);

# Часть 3: Обновление данных

# 1. Измените цены на некоторые товары в лице Products.

# UPDATE Products 
# SET price = 12.99 
# WHERE name = 'Product 1';

# 2. Обновите информацию о количестве товара на складе после создания заказов.

# UPDATE Products 
# SET quantity = quantity - 10 
# WHERE name = 'Product 1';
