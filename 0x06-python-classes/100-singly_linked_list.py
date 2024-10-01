#!/usr/bin/python3
"""
This module defines two classes:
1. Node: A class that defines a node in a singly linked list.
2. SinglyLinkedList: A class that defines a singly linked list and\
        allows insertion of nodes in sorted order.
"""


class Node:
    """Defines a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the Node with data and the next node.

        Agrs:
            data (int): The data to store in the node.
            next_node (Node): The next node in the linked list.\
                    Default is None.

        Raises:
            TypeError: If data is not an integer or if next_node\
                    is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The data value to set.
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node.

        Args:
            value (Node or None): The next node to set.

        Raises:
            TypeError: If value is not a node obeject or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Defines the string representation of the linked list.

        Returns:
            str: A string containing all the node data, one per line.
        """
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position\
                in the list (increasing order).

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            # Insert at the beginning
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Insert in the middle or end
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
