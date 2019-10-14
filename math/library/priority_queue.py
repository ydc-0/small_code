from queue import PriorityQueue

pq = PriorityQueue()
pq.put(4)
pq.put(2)
pq.put(3)
pq.put(2)

while not pq.empty():
    v = pq.get()
    print(v)


class ListNode(object):
    def __init__(self, v):
        self.val = v
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        return "{}, next:{}".format(self.val, self.next)


pq2 = PriorityQueue()
pq2.put(ListNode(4))
pq2.put(ListNode(2))
pq2.put(ListNode(3))

while not pq2.empty():
    n = pq2.get()
    print(n)

