#!/usr/bin/python3

"""Creates a class Node and class SinglyLinkedList"""


class Node:
    """Defines a node of a Singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Fetches self.__data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setter method for self.__data

        Args:
            value (int): value to be stored in self.__data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if ((value is not None) and (type(value) is not Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        temp = self.__head
        if (temp is None) or (self.__head.data >= value):
            new_node.next_node = temp
            self.__head = new_node
            return

        while (temp.next_node is not None):
            if (temp.next_node.data >= value):
                break
            temp = temp.next_node

        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        node_list = []
        temp = self.__head
        while (temp is not None):
            node_list.append(str(temp.data))
            temp = temp.next_node
        ret = "\n".join(node_list)
        return (ret)
