class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        if self.head == None:
            # Если список пустой
            return

        while self.head.value == val:
            # Все случаи если искомый узел первый
            self.head = self.head.next
            if not all:
                return
            if self.head == None:
                return 

        node = self.head
        while node.next != None:
            if node.next.value == val:
                # Удаляем следующий узел
                node.next = node.next.next
                if not all:
                    return
            else:
                # Переходим к следующему узлу
                node = node.next
        # Конец
        return
            

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        node = self.head
        while node is not None:
            node = node.next
            if node.value == afterNode.value:
                newNode.next = node.next
                node.next = newNode
                return True
