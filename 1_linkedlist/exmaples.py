from LinkedList import LinkedList, Node

l = LinkedList()
l.add_in_tail(Node(1))
l.add_in_tail(Node(2))
l.add_in_tail(Node(2))
l.add_in_tail(Node('22'))
l.print_all_nodes()
print(l.len())