from views import CreateMixin, ReadMixin


class SmartPhones(CreateMixin, ReadMixin):
    pass


smartphones = SmartPhones()
print(smartphones.post(title = 'Redmi', description = 'best phone', qty = 10, price = 250))
print(smartphones.post(title = 'Aplle', description = 'best phone', qty = 11, price = 1250))
print(smartphones.post(title = 'Sumsung', description = 'best phone', qty = 12, price = 2250))
print(smartphones.post(title = 'Realmi', description = 'best phone', qty = 13, price = 3250))
print(smartphones.post(title = 'Xiomi', description = 'best phone', qty = 14, price = 4250))

print()
print()
print(smartphones.list())
print()
print(smartphones.list())
print()

