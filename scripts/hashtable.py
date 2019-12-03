#!python

from scripts.linkedlist import LinkedList
from scripts.utility import time_it


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    @time_it
    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) as it loops through each key once"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, _ in bucket.items():
                all_keys.append(key)
        return all_keys

    @time_it
    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) as it loops through each value once"""
        # Loop through all buckets
        # Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for _, value in bucket.items():
                all_values.append(value)
        return all_values

    @time_it
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) as it loops through each item"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    @time_it
    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(1) as it performs one operation
        Formerly O(n) as it looped through each node"""
        # Loop through all buckets
        # Count number of key-value entries in each bucket
        # count = 0
        # for bucket in self.buckets:
        #     for _ in bucket.items():
        #         count += 1
        # return count
        return self.count

    @time_it
    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n/b) as it's the average of the length of each
        bucket"""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        try:
            self.get(key)
        except KeyError:
            return False
        else:
            return True

    @time_it
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n/b) as it's the average of the length of each
        bucket"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # Check if key-value entry exists in bucket
        for buc_key, val in bucket:
            if buc_key == key:
                # If found, return value associated with given key
                return val
        # Otherwise, raise error to tell user get failed
        raise KeyError('Key not found: {}'.format(key))

    @time_it
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(n/b) as it loops over each entry in a bucket and
        replaces the item if it's found, or appends it otherwise"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # Check if key-value entry exists in bucket
        for buc_key, val in bucket:
            if buc_key == key:
                # If found, update value associated with given key
                bucket.replace((buc_key, val), (key, value))
                return
        # Otherwise, insert given key-value entry into bucket
        bucket.append((key, value))
        self.count += 1

    @time_it
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(n/b) as it's the average length of a bucket
        when it looks for an item"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # Check if key-value entry exists in bucket
        for buc_key, val in bucket:
            if buc_key == key:
                # If found, delete entry associated with given key
                bucket.delete((buc_key, val))
                self.count -= 1
                return
        # Otherwise, raise error to tell user delete failed
        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
