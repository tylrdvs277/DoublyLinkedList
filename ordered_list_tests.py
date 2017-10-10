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


    def test_remove_1(self):
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

    def test_remove_2(self):
        """Tests remove by adding three of the same items and removing one.
        Checks that one of the items remains in the list."""
        mylist = OrderedList()
        mylist.add(34)
        mylist.add(34)
        mylist.add(34)
        mylist.remove(34, 2)
        self.assertEqual(mylist.count(34), 1)


    def test_count(self):
        mylist = OrderedList()
        self.assertEqual(mylist.count(10), 0)
        mylist.add(10)
        self.assertEqual(mylist.count(10), 1)
        mylist.add(10)
        self.assertEqual(mylist.count(10), 2)


    def test_sum(self):
        mylist = OrderedList()
        for i in range(11):
            mylist.add(i)
        self.assertEqual(mylist.sum(), 55)


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
        self.assertEqual(mylist.pop(-5), 12)


if __name__ == "__main__":
        unittest.main()