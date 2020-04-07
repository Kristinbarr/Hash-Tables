# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)
        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.
        Fill this in.
        '''

        # compute the index
        index = self._hash_mod(key)
        # save node at current index
        node = self.storage[index]

        # if no collision:
        if node is None:
            # set current node to the generated index
            self.storage[index] = LinkedPair(key, value)
            return

        # if collision: iterate to the end of the LL from the index spot
        # save node in outer scope
        prev = node
        # iterate until the end of the LL
        while node is not None:
            # if current node key == new key, we need to overwrite the value
            if node.key == key:
                node.value = value
                return
            # reassign prev temp variable
            prev = node
            # change node to the current's next node
            node = node.next
        # if we traverse the whole LL and no key matches, insert a new LL
        prev.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        # [idx 0]: (K:2 V:2 N: n )
        # [idx 1]: (K:0 V:0 N:(1)) -> (K:1 V:1 N:(4)) -> (K:4 V:4 N: n )
        # [idx 2]: (K:3 V:3 N: n )

        index = self._hash_mod(key)

        # if the index is in the hash table,
        if self.storage[index] is not None:
            # if the key matches the cur key
            if self.storage[index].key == key:
                # delete the cur value and key
                self.storage[index] = self.storage[index].next
            # else we need to traverse and look for it 
            else:
                # keep track of trailing/prev node
                trailing_node = self.storage[index]
                # keep track of curr node
                cur_node = trailing_node.next

                while cur_node is not None:
                    if cur_node.key == key:
                        trailing_node.next = cur_node.next
                    cur_node = cur_node.next
                    trailing_node = trailing_node.next
        else: 
            print('WARNING: delete key not found')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)

        node = self.storage[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return node

        # if self.storage[index] is not None:
        #     print('RETRIEVED:',self.storage[index].value)
        #     return self.storage[index]
        # else: 
        #     print('WARNING: retrieve key not found')
        #     return


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        # save a copy of the storage
        old_storage = self.storage.copy()
        # set new capicity to be double
        self.capacity *= 2
        # create a new storage that will have new capacity
        self.storage = [None] * self.capacity

        # copy all items over to new doubled capacity hash table
        for item in old_storage:
            if item is not None:
                self.insert(item.key, item.value)


if __name__ == "__main__":
    print("")

    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
