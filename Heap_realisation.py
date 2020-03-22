"""Heap and heap sort realization"""


class Heap:

    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, value):
        self.values.append(value)
        self.size += 1
        self.sift_up(self.size-1)

    def sift_up(self, i):
        while i > 0 and self.values[(i - 1) // 2] > self.values[i]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def extract_min(self):
        if self.size == 0:
            return None
        min_value = self.values[0]
        self.values[0] = self.values[self.size-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return min_value

    def sift_down(self, i):
        if i >= self.size - 1:
            return
        while i * 2 + 1 < self.size:
            j = i
            if self.values[i*2+1] < self.values[i]:
                j = i * 2 + 1
            if i * 2 + 2 < self.size and self.values[i*2+2] < self.values[j]:
                j = i * 2 + 2
            if j == i:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    def convert_list_to_heap(self, a_list):
        for i in range(len(a_list)):
            self.values.append(a_list[i])
            self.size += 1

        for i in range(self.size//2-1, -1, -1):
            self.sift_down(i)


def heap_sort(a_list, start, finish):
    heap = Heap()
    heap.convert_list_to_heap(a_list[start:finish+1])
    for i in range(heap.size):
        a_list[start+i] = heap.extract_min()

