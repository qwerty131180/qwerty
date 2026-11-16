# Experiment 3: Undo/Redo System Using Stack
undo_stack=[]
redo_stack=[]
document=""

def make_change():
    global document
    undo_stack.append(document)

    new_text=input("Enter your change:")
    document+=new_text

    redo_stack.clear()
    print("Changes made to the document.")

def undo():
    global document
    if len(undo_stack)==0:
        print("No change to undo")

    else:
        redo_stack.append(document)
        document=undo_stack.pop()
        print("Undo successful.")

def redo():
    global document
    if len(redo_stack)==0:
        print("No change to redo")

    else:
        undo_stack.append(document)
        document=redo_stack.pop()
        print("Redo successful.")

while True:
    print("\nCurrent document:",document)
    print("1. Make a change")
    print("2. Undo")
    print("3. Redo")
    print("4. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        make_change()
    elif choice==2:
        undo()  
    elif choice==3:
        redo()
    elif choice==4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")        
