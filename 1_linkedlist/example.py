from LinkedList import Node, LinkedList

lst = LinkedList()
lst.add_in_tail(Node(1))
lst.add_in_tail(Node(4))
#lst.add_in_tail(Node(2))
#lst.add_in_tail(Node(2))
#lst.add_in_tail(Node(3))
lst.add_in_tail(Node(2))
lst.add_in_tail(Node(2))
lst.delete(2, all=True)
lst.print_all_in_chain()
