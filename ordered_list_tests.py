# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 4
# Term:        Fall 2017


import unittest
from ordered_list import OrderedList

class TestLab4(unittest.TestCase):


    def test_add(self):
        """Tests the add method by adding two items and making sure they are popped correctly."""
        mylist = OrderedList()
        mylist.add(34)
        mylist.add(10)
        self.assertEqual(mylist.size(), 2)
        self.assertEqual(mylist.pop(0), 10)
        self.assertEqual(mylist.pop(0), 34)


    def test_remove(self):
        """Tests remove by adding two items and removing one.
        Checks for an error when removing an item not in the list."""
        mylist = OrderedList()
        mylist.add(34)
        mylist.add(10)
        mylist.remove(10)
        self.assertEqual(mylist.size(), 1)
        self.assertEqual(mylist.pop(0), 34)
        with self.assertRaises(ValueError):
            mylist.remove(35)


    def test_search_forward(self):
        """Adds two items and makes sure they are found.
        Searches for an item not in the list."""
        mylist = OrderedList()
        mylist.add(34)
        mylist.add(10)
        self.assertTrue(mylist.search_forward(10))
        self.assertTrue(mylist.search_forward(34))
        self.assertFalse(mylist.search_forward(46))


    def test_search_backward(self):
        """Adds two items and makes sure they are found.
        Searches for an item not in the list."""
        mylist = OrderedList()
        mylist.add(34)
        mylist.add(10)
        self.assertTrue(mylist.search_backward(10))
        self.assertTrue(mylist.search_backward(34))
        self.assertFalse(mylist.search_backward(46))


    def test_is_empty(self):
        """Creates a list, adds an item, then removes.
        Tests if empty after every operation."""
        mylist = OrderedList()
        self.assertTrue(mylist.is_empty())
        mylist.add(23)
        self.assertFalse(mylist.is_empty())
        mylist.remove(23)
        self.assertTrue(mylist.is_empty())
        

    def test_size(self):
        """Creates a list, adds an item, then removes.
        Checks size after every operation."""
        mylist = OrderedList()
        self.assertEqual(mylist.size(), 0)
        mylist.add(23)
        self.assertEqual(mylist.size(), 1)
        mylist.remove(23)
        self.assertEqual(mylist.size(), 0)


    def test_pop(self):
        """Adds ten items to the list.
        Tests popping at various indices."""
        mylist = OrderedList()
        for i in range(10, 21):
            mylist.add(i)
        self.assertEqual(mylist.pop(0), 10)
        self.assertEqual(mylist.pop(0), 11)
        self.assertEqual(mylist.pop(4), 16)
        self.assertEqual(mylist.pop(5), 18)
        self.assertEqual(mylist.pop(), 20)
        self.assertEqual(mylist.pop(-2), 17)


if __name__ == "__main__":
        unittest.main()