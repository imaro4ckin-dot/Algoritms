from collections import deque


def reverse_string(text):

    stack = []
    reversed_str = ""


    for char in text:
        stack.append(char)


    while stack:
        reversed_str += stack.pop()

    return reversed_str


original = "Hello, World!"
print(f"Original: {original}")
print(f"Reversed: {reverse_string(original)}")



class TicketQueue:
    def __init__(self):

        self.queue = deque()

    def add_customer(self, name):

        self.queue.append(name)
        print(f"{name} joined the line.")

    def serve_customer(self):

        if len(self.queue) == 0:
            return "No customers in line"


        return self.queue.popleft()



ticket_office = TicketQueue()

ticket_office.add_customer("Alice")
ticket_office.add_customer("Bob")
ticket_office.add_customer("Charlie")

print("\n--- Serving Customers ---")
print(f"Serving: {ticket_office.serve_customer()}")
print(f"Serving: {ticket_office.serve_customer()}")
print(f"Serving: {ticket_office.serve_customer()}")
print(f"Serving: {ticket_office.serve_customer()}")



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_nodes(head):
    count = 0

    current = head
    while current is not None:
        count += 1
        current = current.next
    return count



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")


node1.next = node2
node2.next = node3
node3.next = node4


total = count_nodes(node1)

print(f"Total nodes in the linked list: {total}")