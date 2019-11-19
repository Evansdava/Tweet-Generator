#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list

        # Start at head node
        node = self.head  # O(1) time to assign new variable

        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list

            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable

        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n), because it loops through each node once"""
        count = 0  # O(1) to declare variables
        node = self.head
        while node is not None:  # O(n) to loop through each node once
            count += 1  # O(1) to adjust variables
            node = node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because it sets variables without iterating"""
        # Create new node to hold given item
        new_node = Node(item)
        # Append node after tail, if it exists
        if self.tail is not None:  # O(1) to compare
            self.tail.next = new_node  # O(1) to set variables
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        return new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because it sets variables and doesn't iterate"""
        # Create new node to hold given item
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.head is not None:  # O(1) to compare
            new_node.next = self.head  # O(1) to set variables
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        return new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if the first node satisfies quality
        Worst case running time: O(n) if iterating over every single node"""
        # Loop through all nodes to find item where quality(item) is True
        node = self.head
        while node is not None:  # Loops variable amount, runs in O(1) to O(n)
            # Check if node's data satisfies given quality function
            if quality(node.data):
                return node.data
            else:
                node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if first node is the one to be deleted
        Worst case running time: O(n) if it has to loop through every node"""
        # Loop through nodes to find one whose data matches given item
        node = self.head
        prev_node = self.head
        while node is not None:
            # Update previous node to skip around node with matching data
            if node.data == item:
                # If there is only one element, delete it and set refs
                if self.length() == 1:
                    self.head = None
                    self.tail = None

                # Change head ref if need be
                if node == self.head:
                    self.head = node.next

                # Change tail ref if need be
                if node == self.tail:
                    self.tail = prev_node

                # Update node and next ref of previous node
                prev_node.next = node.next
                node = None
                return
            elif node != prev_node:
                prev_node = prev_node.next
            node = node.next
        # Otherwise raise error to tell user that delete has failed
        raise ValueError(f'Item not found: {item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
