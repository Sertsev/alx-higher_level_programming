#!/usr/bin/python3
""" Singly Linked List """


class Node:
    """ Node class
        - this class creates a node
    """
    def __init__(self, data, next_node=None):
        """initializing value and next node

        Args:
            data (int): an integer value to add to the node
            next_node (Node, optional): a future node. Defaults to None.
        """
        if type(data) != int:
            raise TypeError('data must be an integer')

        self.__data = data

        if next_node is not None and type(next_node) is not Node:
            raise TypeError('next_node must be a Node object')

        self.__next_node = next_node

    @property
    def data(self):
        """a getter function for variable data

        Returns:
            integer: the value of data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter function for data

        Args:
            value (int): it returns an int

        Raises:
            TypeError: raises type error if not int
        """

        if type(self.__data) != int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """a getter function for the node

        Returns:
            Node: returns the future node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next node

        Args:
            value (Node): a Node type node to be setted as a future node

        Raises:
            TypeError: raises if not node type
        """
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list creation class """
    def __init__(self):
        """ initializes the main Node """
        self.__head = None

    def sorted_insert(self, value):
        """sort the nodes decendingly

        Args:
            value (int): an integer value to be sorted and added to the node
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            tmp = self.__head
            nn = Node(value)

            if tmp.data > nn.data:
                nn.next_node = tmp
                self.__head = nn
            else:
                while tmp.next_node is not None:
                    if nn.data < tmp.next_node.data:
                        nn.next_node = tmp.next_node
                        tmp.next_node = nn
                        return
                    tmp = tmp.next_node
                tmp.next_node = nn

    def __str__(self):
        """a string representation of the singly linked list

        Returns:
            string: a list of string data of the nodes
        """
        tmp = self.__head
        string = ""

        while tmp is not None:
            string += str(tmp.data)

            if tmp.next_node is not None:
                string += '\n'
            tmp = tmp.next_node

        return string
