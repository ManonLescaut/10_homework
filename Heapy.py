#!/usr/bin/env python
# coding: utf-8

# In[109]:


class Heap():
    def __init__(self):
        self.heaplist = [] #значения узлов кучи
        self.heapsize = 0  #размер кучи
     
    # размер кучи
    def __len__(self):
        return self.heapsize
    
    # доступ к элементу кучи по индексу
    def __getitem__(self, idx): 
        if idx >= self.heapsize:
            raise IndexError("Index out of range")
        return self.heaplist[idx]
    
    # итератор
    def __iter__(self): 
        for i in range(self.heapsize):
            yield self.heaplist[i]
    
    # просеивание одного элемента 
    def heapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        if left < self.heapsize and self.heaplist[left] > self.heaplist[i]:
            largest = left
        else:
            largest = i
        if right < self.heapsize and self.heaplist[right] > self.heaplist[largest]:
            largest = right
        if largest != i:
            self.heaplist[i], self.heaplist[largest] = self.heaplist[largest], self.heaplist[i]
            self.heapify(largest)
     
    # создание кучи из массива
    def make_heap(self, lst):
        self.heaplist = lst
        self.heapsize = len(lst)
        for i in range(self.heapsize//2-1, -1, -1):
            self.heapify(i)
    
    # замена элемента 
    def insert(self, i, val):
        if i >= self.heapsize:
            raise IndexError()
        if self.heaplist[i] <= val:
            self.heaplist[i] = val
            while i > 0 and self.heaplist[i//2] < self.heaplist[i]:
                self.heaplist[i//2], self.heaplist[i] = self.heaplist[i], self.heaplist[i//2]
                i = i//2
        elif self.heaplist[i] > val:
            self.heaplist[i] = val
            self.heapify(i)
                
    # добавление в кучу с сохранением структуры
    def add(self, x): 
        self.heapsize += 1
        self.heaplist.append(float('-inf'))
        self.insert(self.heapsize-1, x)
    
    # извлечение из корня кучи с сохранением структуры
    def pop(self, x): 
        if self.heapsize < 1:
            return ('Пустая куча')
        max_el = self.heaplist[0]
        self.heaplist[0] = self.heaplist(self.heapsize)
        self.heapsize -= 1
        self.heapify(0)
        return max_el

# пирамидальная сортировка
def heap_sort_decorator(make_heap): #честно говоря, я не знаю, где здесь еще использовать декоратор
    def sorting_wrap(lst):
        helper_heap = Heap()
        helper_heap.make_heap(lst)
        for i in range(helper_heap.heapsize-1, -1, -1):
            lst[i] = h.heaplist[i]
            helper_heap.heaplist[i], helper_heap.heaplist[0] = helper_heap.heaplist[0], helper_heap.heaplist[i]
            helper_heap.heapsize -= 1
            helper_heap.heapify(0)
    return sorting_wrap
    
    
# восстановление структуры кучи
@heap_sort_decorator
def heap_sort(lst):
    self.heaplist = lst
    self.heapsize = len(lst)
    for i in range(self.heapsize//2-1, -1, -1):
        self.heapify(i)


# In[ ]:




