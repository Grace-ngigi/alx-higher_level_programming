#!/usr/bin/python3


class Node:
    """A node class of a singly linked list"""
    def __init__(self, data, next_node=None):
        """
        Initialize a Node instance

        Args:
            data(int): data to be stored in the node.
            next_node(Node): next node in the linked list.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve data stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        set the data stored in the node.

        Args:
            value(int): new data to be stored u the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        set the next node in the linked list.
        Args:
            value(int): The next node to be set.
        Raises:
            TypeError: if the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    """A node class of a singly linked list"""
    def __init__(self):
        """
        Initialize an empty SinglyLinkedList instance.

        Attributes:
            head (Node): The head (first node) of the linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted.

        Inserts a new Node with the given value into the linked list while
        maintaining the list's sorted order.

        Returns:
            None
        """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Get a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return ('\n'.join(result))
