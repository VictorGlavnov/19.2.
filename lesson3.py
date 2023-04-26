seq_num = input('Введите последовательность чисел через пробел:')
user_num = int(input('Введите число:'))

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if not is_int(seq_num):
    print('Некорректно введены данные!')
else:
    seq_num = seq_num.split()

list_seq_num = list(map(int,seq_num))


def sort():
    for i in range(len(list_seq_num)):
        for j in range(len(list_seq_num) - i - 1):
            if list_seq_num[j] > list_seq_num[j + 1]:
                list_seq_num[j], list_seq_num[j + 1] = list_seq_num[j + 1], list_seq_num[j]
    return list_seq_num

list_seq_num.sort()
print(f'Сортировка списка по возрастанию: {list_seq_num}')

def binary_search(list_seq_num, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if list_seq_num[middle] == element:
            return middle
        elif element < list_seq_num[middle]:
            return binary_search(list_seq_num, element, left, middle - 1)
        else:
            return binary_search(list_seq_num, element, middle + 1, right)
    except IndexError:
        return 'В списке нет введенного числа'

if not binary_search(list_seq_num, user_num, 0, len(list_seq_num)):
    rI = min(list_seq_num, key=lambda x: (abs(x - user_num), x))
    ind = list_seq_num.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_num:
        print(f'''Ближайший меньший элемент =  {rI}, его индекс: {ind}
Ближайший больший элемент =  {list_seq_num[max_ind]}, индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке отсутствет ближайший меньший элемент 
Ближайший больший элемент: {rI}, индекс: {list_seq_num.index(rI)}''')
    elif rI > number:
        print(f'''Ближайший больший элемент: {rI}, его индекс: {list_seq_num.index(rI)}
Ближайший меньший элемент: {list_seq_num[min_ind]}, его индекс: {min_ind}''')
    elif list_seq_num.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_seq_num.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_seq_num, user_num, 0, len(list_seq_num))}')