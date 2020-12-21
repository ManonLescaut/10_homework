#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class GetMean(Exception):
    pass

class GetDisp(Exception):
    pass

class GetNum(Exception):
    pass

def statistics_coroutine():
    print('Starting coroutine')
    print('''Введите число. Чтобы узнать количество введенных чисел, введите "Количество". Чтобы узнать среднее, 
             введите "Среднее". Чтобы узнать дисперсию, введите "Дисперсия. "''')
    num = 0
    summ = 0
    mean = 0
    summ_kv = 0
    mean_kv = 0
    disp = 0
    try:
        while True:
            try:
                x = yield
                num += 1
                summ += x
                summ_kv += x**2
                mean = summ/num
                mean_kv = summ_kv/num
                disp = mean_kv - mean**2
            except GetMean:
                yield mean
            except GetDisp:
                yield disp
            except (GetNum):
                yield num
    finally:
        print("Coroutine stopped")

coroutine = statistics_coroutine()
next(coroutine)
i = 0
while i != 'Стоп':
    i = input('Число или команда: ')
    if i.isdigit():
        i = int(i)
        coroutine.send(i)
    if i == 'Среднее':
        print("Текущее среднее:", coroutine.throw(GetMean))
        next(coroutine)
    if i == 'Дисперсия':
        print("Текущая дисперсия:", coroutine.throw(GetDisp))
        next(coroutine)
    if i == 'Количество':
        print("Количество элементов:", coroutine.throw(GetNum))
        next(coroutine)
print()
coroutine.close()

