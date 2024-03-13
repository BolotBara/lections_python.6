ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 16, 17, 23]
left = 0
right  = len(ls) - 1
mid = len(ls) // 2
value = int(input('Введите число: '))

while ls[mid] != value and left <= right:
    if value < ls[mid]:
        right = mid -1
    else:
        left = mid +1
    mid = (left + right) // 2

if left > right:
    print('Not')
else:
    print(f'{value} = {ls[mid]}')



