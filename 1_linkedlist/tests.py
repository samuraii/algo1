import unittest
from LinkedList import LinkedList, Node

class TestLinkedListListLen(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_list_len_0_elements(self):
        assert self.l.len() == 0, 'Длина списка должна быть равна 0'

    def test_list_len_100000_elements(self):
        for i in range(100000):
            self.l.add_in_tail(Node(i))
        assert self.l.len() == 100000, 'Длина списка должна быть равна 100000'

    def test_list_len_3_elements(self):
        self.l.add_in_tail(Node(1))
        self.l.add_in_tail(Node(1))
        assert self.l.len() == 2, 'Длина списка должна быть равна 2'

    def test_list_len_1_element(self):
        self.l.add_in_tail(Node(1))
        assert self.l.len() == 1, 'Длина списка должна быть равна 1'
    
class TestLinkedListFindAll(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()
    
    def test_find_all_empty_list(self):
        nodes = self.l.find_all(1)
        assert len(nodes) == 0, 'Длина списка должна быть равна 0'
    
    def test_find_all_0_elements(self):
        self.l.add_in_tail(Node(2))
        nodes = self.l.find_all(1)
        assert len(nodes) == 0, 'Длина списка должна быть равна 0'
    
    def test_find_all_correct_element(self):
        self.l.add_in_tail(Node(2))
        self.l.add_in_tail(Node(88))
        self.l.add_in_tail(Node(2))
        self.l.add_in_tail(Node(1))
        self.l.add_in_tail(Node(88))
        self.l.add_in_tail(Node('S'))
        nodes = self.l.find_all(88)
        assert len(nodes) == 2, 'Длина списка должна быть равна 1'
        assert nodes[0].value == 88, 'Элемент должен быть равен 88'
        assert nodes[1].value == 88, 'Элемент должен быть равен 88'

class TestLinkedListClean(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()
    
    def test_clean_list(self):
        self.l.add_in_tail(Node(2))
        self.l.add_in_tail(Node(88))
        self.l.add_in_tail(Node(2))
        self.l.add_in_tail(Node(1))
        self.l.add_in_tail(Node(88))
        self.l.add_in_tail(Node('S'))
        assert self.l.len() != 0, 'После наполнения список должен быть не 0 длины'
        self.l.clean()
        assert self.l.len() == 0, 'После очистки длина списка должна быть 0'
    
    def test_list_len_100000_elements(self):
        for i in range(100000):
            self.l.add_in_tail(Node(i))
        assert self.l.len() != 0, 'После наполнения список должен быть не 0 длины'
        self.l.clean()
        assert self.l.len() == 0, 'Длина списка должна быть равна 0'

if __name__ == '__main__':
    unittest.main()
