def insertion_sort(A):
  """Алгоритм сортировки вставкой от большего к меньшему"""
    for j in range(len(A)-1): # перебираем элементы в массиве
        key = A[j+1] # берем второй элемент массива
        i = j # записываем индекс левого элемента от выбранного ранее
        while ( (i > -1) & (A[i] < key) ): # повторяем пока не переберем все элементы или пока не элемент не окажется меньше выбранного
            A[i+1] = A[i] # меняем меньшее значение на большее
            i = i - 1 # переходим к следующему индексу
        A[i+1] = key # меняем меньшее значение на большее
    return A # возвращаем отсортированный массив
print(insertion_sort([1,2,3])) # проверка
