# Define a class called Node to represent a node in a linked list
class Node:
    # Initialize the Node object with data and set the next pointer to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class called LinkedList to represent a singly linked list
class LinkedList:
    # Initialize the linked list with an empty head node
    def __init__(self):
        self.head = None

    # Display the elements in the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Invalid position")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Insert a new node with the given data at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete_at_begin(self):
        if not self.head:
            print("List is empty, cannot delete.")
            return
        self.head = self.head.next
    def delete_at_end(self):
        if not self.head:
            print("List is empty, cannot delete.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            if current is None or current.next is None:
                print("Invalid position")
                return
            current = current.next
        current.next = current.next.next

    # Delete a node with the given data from the linked list
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                print(f"Element {data} found at position {position}")
                return
            current = current.next
            position += 1
        print(f"Element {data} not found in the list")
    def countof(self):
        current=self.head
        c=0
        while current:
            c +=1
            current=current.next
        print('No of Nodes', c)
# Example usage
# Create an instance of the LinkedList class
linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_position(10,1)
linked_list.insert_at_begin(12)
linked_list.display()
linked_list.search(2)
linked_list.delete_at_begin()
linked_list.delete_at_end()
linked_list.display()
linked_list.insert_at_end(4)
linked_list.delete_at_position(0)
# Display the initial linked list
print("Initial Linked List:")
linked_list.display()
linked_list.countof()
# Insert a new node with data 5 into the linked list
linked_list.insert_at_end(5)
print("After inserting a new node (5):")
linked_list.display()
# Delete a node with data 2 from the linked list
#linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display() 
