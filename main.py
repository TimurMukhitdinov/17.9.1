array = input('Введите числа через пробел от 0 до 100: ').split()
L = list(map(int, array))  # преобразовываем последовательность в список

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
print('Отсортированный массив:', merge_sort(L))
print('Количество элементов в  массиве:', len(merge_sort(L)))



def binary_search(L, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if L[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < L[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(L, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(L, element, middle + 1, right)

while True:
    try:
        element = int(input('Введите число от 0 до 100: '))
        if element < 0 or element > 100:
            raise Exception
        break
    except ValueError:
        print('Нужно ввести число!')
    except Exception:
        print('Неправильный диапазон!')

print(binary_search(L, element, 0, len(L)))