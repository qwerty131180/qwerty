# Experiment 4: Student Record Management Using Singly Linked List
class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None
 
 
class StudentList:
    def __init__(self):
        self.head = None
 
    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
 
    def search(self, roll):
        temp = self.head
        while temp is not None:
            if temp.roll == roll:
                return temp
            temp = temp.next
        return None
 
    def delete(self, roll):
        temp = self.head
        previous = None
        while temp is not None and temp.roll != roll:
            previous = temp
            temp = temp.next
        if temp is None:
            print("Student Not Found")
            return
        if previous is None:            # deleting the first node
            self.head = temp.next
        else:
            previous.next = temp.next
 
    def update(self, roll, new_name, new_marks):
        student = self.search(roll)
        if student is None:
            print("Student Not Found")
        else:
            student.name = new_name
            student.marks = new_marks
 
    def sort(self, descending=False):
        # Bubble sort on the linked list (swap the data, not the nodes)
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp is not None and temp.next is not None:
                if descending:
                    wrong_order = temp.marks < temp.next.marks
                else:
                    wrong_order = temp.marks > temp.next.marks
                if wrong_order:
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
 
    def display(self):
        temp = self.head
        while temp is not None:
            print(" [" + str(temp.roll) + ", " + temp.name + ", " + str(temp.marks) + "]", end=" ->")
            temp = temp.next
        print(" NULL")
 
 
students = StudentList()
students.add(101, "Amit", 85)
students.add(102, "Ravi", 72)
students.add(103, "Neha", 91)
students.add(104, "Sara", 64)
 
print("Records:")
students.display()
 
found = students.search(103)
print("Search 103:", found.name, found.marks)
 
students.update(102, "Ravi", 78)
print("After update of 102:")
students.display()
 
students.delete(104)
print("After delete of 104:")
students.display()
 
students.sort()
print("Ascending by marks:")
students.display()
 
students.sort(descending=True)
print("Descending by marks:")
students.display()
 
students.delete(999)
 