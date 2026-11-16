# Experiment 8: Binary Search Tree Operations

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    else:
        print("Duplicate value not allowed")

    return root


def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    elif key < root.data:
        return search(root.left, key)

    else:
        return search(root.right, key)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children
        else:
            temp = root.right

            while temp.left is not None:
                temp = temp.left

            root.data = temp.data
            root.right = delete(root.right, temp.data)

    return root


root = None

while True:
    print("\n--- Binary Search Tree ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value to insert: "))
        root = insert(root, data)

    elif choice == 2:
        data = int(input("Enter value to delete: "))
        root = delete(root, data)
        print("Deletion operation completed")

    elif choice == 3:
        data = int(input("Enter value to search: "))

        if search(root, data):
            print("Value found")
        else:
            print("Value not found")

    elif choice == 4:
        if root is None:
            print("Tree is empty")
        else:
            print("BST in sorted order:")
            inorder(root)
            print()

    elif choice == 5:
        print("Program terminated")
        break

    else:
        print("Invalid choice")