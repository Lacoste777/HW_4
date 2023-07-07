# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def replacement_with_s(*lids):
    lids = list(lids)
    temp = []
    for i in range(len(lids)):
        if lids[i].endswith('s') and lids[i] != 's':
            temp.append(lids[i])
            lids[i] = None
    for i in range(len(lids)):
        if lids[i] is not None:
            lids[i] += ''.join([i for i in temp])
    return lids


print(replacement_with_s('bis', 'ros', 's', 'row'))