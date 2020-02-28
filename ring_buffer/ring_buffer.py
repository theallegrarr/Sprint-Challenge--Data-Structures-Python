from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if(self.storage.length < self.capacity):
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            drop_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if drop_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        count = self.storage.length
        while count > 0:
            value = self.storage.remove_from_head()
            list_buffer_contents.append(value)
            self.storage.add_to_tail(value)
            count -= 1
        
        return list_buffer_contents

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current_index = 0
    def append(self, item):
        #add item to current index
        self.storage[self.current_index] = item
        #increment index
        self.current_index += 1
        #if index is at capacity, move it back to the beginning
        if self.current_index == self.capacity:
            self.current_index = 0
    def get(self):
        #remove all empty elements with list comprehension and return list
        return [i for i in self.storage if i]
