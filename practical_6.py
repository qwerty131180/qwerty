size=10
hash_table=[-1]*size

def insert():
    key=int(input("Enter the key to insert:"))
    index=key%size

    for i in range(size):
        new_index=(index+i)%size
        if hash_table[new_index]==-1:
            hash_table[new_index]=key
            print("Key inserted at index:", new_index)
            return
    print("Hash table is full.")

def search():
    key=int(input("Enter the key to search:"))
    index=key%size

    for i in range(size):
        new_index=(index+i)%size
        if hash_table[new_index]==key:
            print("Key found at index:", new_index)
            return
        print("Key not found in the hash table.")

def delete():
    key=int(input("Enter the key to delete:"))
    index=key%size

    for i in range(size):
        new_index=(index+i)%size

        if hash_table[new_index]==key:
            hash_table[new_index]=-1
            print("Key deleted from the hash table.")
            return
        print("Key not found in the hash table.")

def display():
    print("Hash Table content:")
    for i in range(size):
        print(i,":",hash_table[i])

while True:
    print("\nHash Table Menu:")
    print("1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Hash Table")
    print("5. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        insert()
    elif choice==2:
        search()
    elif choice==3:
        delete()
    elif choice==4:
        display()
    elif choice==5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.") 