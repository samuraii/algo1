import unittest
from LinkedList import LinkedList, Node

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_list_len_0_elements(self):
        assert self.l.len() == 0

    def test_list_len_100000_elements(self):
        for i in range(100000):
            self.l.add_in_tail(Node(i))
        assert self.l.len() == 100000

    def test_list_len_3_elements(self):
        self.l.add_in_tail(Node(1))
        self.l.add_in_tail(Node(1))
        assert self.l.len() == 2, 'Длина списка должна быть равна 2'

    def test_list_len_1_element(self):
        self.l.add_in_tail(Node(1))
        assert self.l.len() == 1, 'Длина списка должна быть равна 1'

if __name__ == '__main__':
    unittest.main()
