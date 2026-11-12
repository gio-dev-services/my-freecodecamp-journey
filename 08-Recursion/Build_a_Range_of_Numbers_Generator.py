def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        lista = []
        lista.append(start_num)
        return lista
    lista = range_of_numbers(start_num + 1, end_num)
    lista.append(start_num)
    lista.sort()
    return lista
   
print(range_of_numbers(3, 9))
