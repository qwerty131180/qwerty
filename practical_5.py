# Experiment 5: Hash Table Using Division Method and Chaining

size=10
hash_table=[[] for i in range(size)]

def insert(key,value):
    index=key%size

    hash_table[index].append((key,value))
    print("Key-value pair inserted at index:", index)
    return

def search(key):
    index=key%size

    for k,v in hash_table[index]:
        if k==key:
            print("Key found at index:", index, "with value:", v)
            return
    print("Key not found in the hash table.")

def delete(key):
    index=key%size

    for item in hash_table[index]:
        if item[0]==key:
            hash_table[index].remove(item)
            print("Key deleted from the hash table.")
            return
    print("Key not found in the hash table.")    


def display():
    print("Hash Table content:")
    for i in range(size):
        print(i,":",hash_table[i])

while True:
    print("\nHash Table Menu:")
    print("1. Insert Key-Value Pair")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Hash Table")
    print("5. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        key=int(input("Enter the key to insert:"))
        value=input("Enter the value to insert:")
        insert(key,value)
    elif choice==2:
        key=int(input("Enter the key to search:"))
        search(key)
    elif choice==3:
        key=int(input("Enter the key to delete:"))
        delete(key)
    elif choice==4:
        display()
    elif choice==5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")        