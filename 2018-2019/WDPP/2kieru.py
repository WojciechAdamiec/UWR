class auto:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None


def add_end(list, value):
    c = 1
    while c.next is not None:
        c = c.next
    c.next = auto(value)
    c.next.prev
