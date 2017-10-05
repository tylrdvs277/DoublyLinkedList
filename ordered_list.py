# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 4
# Term:        Fall 2017


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

class OrderedList:

    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.set_next(self.sentinel)
        self.sentinel.set_prev(self.sentinel)
        self.num_items = 0

    def add(self, item):
        current = self.sentinel.get_next()
        temp = Node(item)
        while current.get_data() != None and current.get_data() < item:
            current = current.get_next()
        temp.set_next(current)
        current.get_prev().set_next(temp)
        temp.set_prev(current.get_prev())
        current.set_prev(temp)
        self.num_items += 1

    def remove(self, item):
        current = self.sentinel.get_next()
        while current.get_data() != None:
            if current.get_data() == item:
                current.get_prev().set_next(current.get_next())
                current.get_next().set_prev(current.get_prev())
                self.num_items -= 1
                return
            current = current.get_next()
        raise ValueError

    def search_forward(self, item):
        current = self.sentinel.get_next()
        while current.get_data() != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def search_backward(self, item):
        current = self.sentinel.get_prev()
        while current.get_data() != None:
            if current.get_data() == item:
                return True
            current = current.get_prev()
        return False

    def is_empty(self):
        return self.num_items == 0

    def size(self):
        return self.num_items

    def index(self, item):
        idx = 0 
        current = self.sentinel.get_next()
        while current.get_data() != None:
            if current.get_data() == item:
                return idx
            current = current.get_next()
            idx += 1
        raise IndexError

    def pop(self):
        current = self.sentinel.get_prev()
        current.get_prev().set_next(current.get_next())
        current.get_next().set_prev(current.get_prev())
        self.num_items -= 1

    def pop(self, pos):
        if not (0 <= pos <= self.num_items - 1):
            raise IndexError
        if pos <= self.num_items / 2:
            idx = 0
            step = 1
            current = self.sentinel.get_next()
        else:
            idx = self.num_items - 1
            step = -1
            current = self.sentinel.get_prev()
        while idx != pos:
            if step == 1:
                current = current.get_next()
            else:
                current = current.get_prev()
            idx += step
        data = current.get_data()
        self.num_items -= 1
        current.get_prev().set_next(current.get_next())
        current.get_next().set_prev(current.get_prev())
        return data
