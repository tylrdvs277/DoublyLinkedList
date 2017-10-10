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
        """Creates a new oredered list using a sentinel node implementation."""
        self.sentinel = Node(None)
        self.sentinel.set_next(self.sentinel)
        self.sentinel.set_prev(self.sentinel)
        self.num_items = 0

    def add(self, item):
        """Adds a new item to the list in numerical order."""
        """Takes a new number (float or int).
        Modifies the existing list and returns None."""
        current = self.sentinel.get_next()
        temp = Node(item)
        while (current.get_data() != None and 
               current.get_data() < item):
            current = current.get_next()
        temp.set_next(current)
        current.get_prev().set_next(temp)
        temp.set_prev(current.get_prev())
        current.set_prev(temp)
        self.num_items += 1

    def remove(self, item, times = 1):
        """Removes a specific item in the first place it occurs (from front)."""
        """Takes an item to be removed.
        Modifies the existing list and returns None. Raises an error if the item isn't in the list."""
        removed = 0
        current = self.sentinel.get_next()
        while (current.get_data() != None and 
               removed < times and 
               current.get_data() <= item):
            if current.get_data() == item:
                current.get_prev().set_next(current.get_next())
                current.get_next().set_prev(current.get_prev())
                self.num_items -= 1
                removed += 1
            current = current.get_next()
        if removed < times:
            raise ValueError

    def count(self, item):
        """Determines the amount of times an item appears in a list."""
        """Takes an item to be counted.
        Returns an int representing the amount of times the item appears."""
        current = self.sentinel.get_next()
        count = 0
        while (current.get_data() != None and 
               current.get_data() <= item):
            if current.get_data() == item:
                count += 1
            current = current.get_next()
        return count

    def search_forward(self, item):
        """Checks for an item in the list starting from the front."""
        """Takes an item to look for.
        Returns True if the item is in the list and False otherwise."""
        current = self.sentinel.get_next()
        while (current.get_data() != None and
               current.get_data() < item):
            current = current.get_next()
        return current.get_data() == item

    def search_backward(self, item):
        """Checks for an item in the list starting from the back."""
        """Takes an item to look for.
        Returns True if the item is in the list and False otherwise."""
        current = self.sentinel.get_prev()
        while (current.get_data() != None and
               current.get_data() > item):
            current = current.get_prev()
        return current.get_data() == item

    def is_empty(self):
        """Checks if there are any elements in the list."""
        """Takes no parameters.
        Returns True if there are no items and False otherwise."""
        return self.num_items == 0

    def size(self):
        """Checks the amount of elements in the list."""
        """Takes no parameters.
        Returns an int representing the amount of items in the list."""
        return self.num_items

    def sum(self):
        total = 0
        current = self.sentinel.get_next()
        while current.get_data() != None:
            total += current.get_data()
            current = current.get_next()
        return total

    def index(self, item):
        """Determines the index of an item in the list."""
        """Takes an item to look for in the list.
        Returns an int representing the position of the item in the list."""
        idx = 0 
        current = self.sentinel.get_next()
        while (current.get_data() != None and
               current.get_data() < item):
            current = current.get_next()
            idx += 1
        if current.get_data() == item:
            return idx
        raise ValueError

    def pop(self, pos = None):
        """Removes an item at a given position and returns it."""
        """Takes an int representing an index to remove from.
        Returns the value at that position and modifies the list."""
        if pos == None:
            pos = self.num_items - 1
        if pos < 0:
            pos += self.num_items
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
        self.num_items -= 1
        current.get_prev().set_next(current.get_next())
        current.get_next().set_prev(current.get_prev())
        return current.get_data()