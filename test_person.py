import unittest
import person


class TestPerson(unittest.TestCase):
    # TODO
    def test_get_full_name(self):
        p1 = Person('Bill', 'Gates', 15)
        p2 = Person('Steve', 'Jobs', 25)
        self.assertEqual(p1.get_full_name(), 'Bill Gates')
        self.assertEqual(p2.get_full_name(), 'Steve Jobs')
