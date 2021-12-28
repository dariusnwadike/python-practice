import sys

from node import Node


class List:

    def __init__(self, new_list=None):
        if new_list is None or new_list.is_empty():
            self.size = 0
            self.list = Node()
        else:
            temp_list = List()
            for i in range(new_list.get_size()):
                temp_list.add(new_list.get(i))
            self.list = Node()
            self.size = 0
            for i in range(new_list.get_size()):
                self.add(temp_list.get(i))

    def add(self, obj):
        if obj is None:
            sys.exit("input is null")
        else:
            if self.size == 0:
                self.list.set_data(obj)
                self.size += 1
            else:
                pointer = self.list
                for i in range(self.size):
                    if pointer.get_next_node() is None:
                        pointer.set_next_node(Node(obj))
                    pointer = pointer.get_next_node()
                self.size += 1

    def add_index(self, index, obj):
        if obj is None:
            sys.exit("input is null")
        elif index < 0 or index > self.size:
            sys.exit("index out of bounds")
        else:
            temp_list = List()
            pointer = self.list
            for i in range(self.size + 1):
                if i != index:
                    temp_list.add(pointer.get_data())
                    pointer = pointer.get_next_node()
                else:
                    temp_list.add(obj)
            self.clear()
            for i in range(temp_list.get_size()):
                self.add(temp_list.get(i))

    def add_list(self, new_list):
        if new_list is None or new_list.is_empty():
            sys.exit("list is null/empty")
        else:
            temp_list = List()
            for i in range(self.size):
                temp_list.add(self.get(i))
            for i in range(new_list.get_size()):
                temp_list.add(new_list.get(i))
            self.clear()
            for i in range(temp_list.get_size()):
                self.add(temp_list.get(i))

    def add_list_at_index(self, index, new_list):
        if new_list is None or new_list.is_empty():
            sys.exit("list is null/empty")
        elif index < 0 or index > self.size:
            sys.exit("index out of bounds")
        else:
            temp_list = List()
            pointer = self.list
            for i in range(self.size + 1):
                if i != index:
                    temp_list.add(pointer.get_data())
                    pointer = pointer.get_next_node()
                else:
                    temp_list.add_list(new_list)
            self.clear()
            for i in range(temp_list.get_size()):
                self.add(temp_list.get(i))

    def clear(self):
        self.list = Node()
        self.size = 0

    def contains(self, obj):
        return_value = False
        if obj is None:
            sys.exit("input is null")
        else:
            pointer = self.list
            for i in range(self.size):
                if obj == pointer.get_data():
                    return_value = True
                else:
                    pointer = pointer.get_next_node()
        return return_value

    def distinct(self):
        temp_list = List()
        pointer = self.list
        for i in range(self.size):
            if not temp_list.contains(pointer.get_data()):
                temp_list.add(pointer.get_data())
            pointer = pointer.get_next_node()
        return temp_list

    def get(self, index):
        return_value = None
        if index < 0 or index >= self.get_size():
            sys.exit("index out of bounds")
        else:
            pointer = self.list
            for i in range(self.size):
                if pointer.get_next_node() is not None and i == index:
                    return_value = pointer.get_data()
                elif pointer.get_next_node() is None and i == self.size - 1:
                    return_value = pointer.get_data()
                else:
                    pointer = pointer.get_next_node()
        return return_value

    def get_size(self):
        return self.size

    def index_of(self, obj):
        index = -1
        if obj is None:
            sys.exit("input is null")
        else:
            pointer = self.list
            for i in range(self.size):
                if pointer.get_data() == obj:
                    index = i
                    break
                else:
                    pointer = pointer.get_next_node()
        return index

    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False

    def remove(self, index):
        pointer = self.list
        pointer2 = pointer
        temp_list = List()
        if index < 0 or index >= self.size:
            sys.exit("index out of bounds")
        else:
            for i in range(self.size):
                if i != index:
                    pointer = pointer.get_next_node()
                else:
                    pointer.set_data(None)
                    break
            pointer3 = pointer2
            for i in range(self.size):
                if pointer3.get_data() is not None:
                    temp_list.add(pointer3.get_data())
                pointer3 = pointer3.get_next_node()
            self.clear()
            for i in range(temp_list.get_size()):
                self.add(temp_list.get(i))

    def reverse(self):
        temp_list = List()
        temp_list2 = List()
        pointer = self.list
        for i in range(self.size):
            temp_list.add(pointer.get_data())
            pointer = pointer.get_next_node()
        for i in range(self.size - 1, -1, -1):
            temp_list2.add(temp_list.get(i))
        return temp_list2

    def set(self, index, obj):
        if obj is None:
            sys.exit("object is null")
        elif index < 0 or index >= self.size:
            sys.exit("index out of bounds")
        else:
            pointer = self.list
            for i in range(self.size):
                if i == index:
                    pointer.set_data(obj)
                    break
                else:
                    pointer = pointer.get_next_node()

    def __str__(self):
        return_value = ""
        sep = ", "
        counter = 0
        pointer = self.list
        for i in range(self.size):
            counter += 1
            if counter == self.size:
                return_value += str(pointer.get_data())
            else:
                return_value += str(pointer.get_data()) + sep
            pointer = pointer.get_next_node()
        return return_value

    def to_list(self):
        return_list = []
        for i in range(self.size):
            return_list.append(self.get(i))
        return return_list


class Test:
    l1 = List()
    print(l1.is_empty())
    l1.add("test1")
    l1.add("test2")
    l1.add("test3")
    l1.add("test4")
    l1.add("test5")
    l1.add_index(3, "test6")
    print(l1.get(3))
    print(l1.index_of("test6"))
    print(l1)
    print(l1.get_size())
    list_reverse = l1.reverse()
    print(list_reverse)
    l1.set(0, "test11")
    print(l1)
    l2 = List()
    l2.add_list(l1)
    l2.add_list_at_index(3, list_reverse)
    print(l2)
    print(l2.size)
    no_repeats = l2.distinct()
    print(no_repeats)
    print(no_repeats.get_size())
    print(no_repeats.index_of("test1"))
    print(l2)
    l3 = List(l2)
    print(l3)
    print(l3.get_size())
    python_list = l3.to_list()
    print(python_list)
    l4 = List()
    l4.add(1)
    l4.add(2)
    l4.add(3)
    l4.add(4)
    l4.add(5)
    python_list2 = l4.to_list()
    l4.add_list_at_index(3, l3)
    print(python_list2)
    print(l4)
    l5 = l4.distinct()
    print(l5)
