# Experiment 1: Linear Search and Binary Search
accounts = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

search_acc = int(input("Enter account ID to search: "))

def linear_search(accounts, search_acc):
    for i in range(len(accounts)):
        if accounts[i] == search_acc:
            return i
    return -1

def binary_search(accounts, search_acc):
    st = 0
    end = len(accounts) - 1

    while st <= end:
        mid = (st + end) // 2

        if accounts[mid] == search_acc:
            return mid
        elif search_acc < accounts[mid]:
            end = mid - 1
        else:
            st = mid + 1

    return -1

print("\nLINEAR SEARCH")
index = linear_search(accounts, search_acc)

if index != -1:
    print("Account found at index", index)
else:
    print("Account not found")

print("\nBINARY SEARCH")
index = binary_search(accounts, search_acc)

if index != -1:
    print("Account found at index", index)
else:
    print("Account not found")