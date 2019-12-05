import scripts.linkedlist as ll


class Queue():
    """A data structure for FIFO operations"""

    def __init__(self, items=None):
        """Initialize a linked list and append given items, if any"""
        self.list = ll.LinkedList(items)
        self.len = 0

    def __str__(self):
        """Returns a string representation of the queue"""
        return " ".join(self)

    def __iter__(self):
        """Returns an iterable object for the queue"""
        return self.list.__iter__()

    def length(self):
        """Return the length of the queue"""
        return self.len

    def enqueue(self, item):
        """Put an item into the back of the queue"""
        self.list.append(item)
        self.len += 1

    def dequeue(self):
        """Return and remove the first item in the queue"""
        item = self.list.head
        if self.length() > 0:
            self.list.delete(item.data)
            self.len -= 1
            return item.data
        else:
            raise RuntimeError("Cannot dequeue from an empty queue.")


def test_queue():
    """Basic tests to make sure everything functions"""
    q = Queue()
    print(f"Queue: {q}")

    print("\nTesting enqueue:")
    for item in ['A', 'B', 'C']:
        print("enqueue({!r})".format(item))
        q.enqueue(item)
        print(f"Queue: {q}")
    
    print("\nTesting iteration and typecasting:")
    for i in q:
        print(i)
    print("Tuple:")
    print(tuple(q))
    print("List:")
    print(list(q))
    print("String:")
    print(str(q))

    print("\nTesting dequeue:")
    for _ in range(3):
        item = q.dequeue()
        print("dequeued {!r}".format(item))
        print(f"Queue: {q}")

    print("\nTesting dequeue on empty queue:")
    try:
        q.dequeue()
    except RuntimeError:
        print("Error successfully raised")


if __name__ == '__main__':
    test_queue()
