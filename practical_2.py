# Experiment 2: Employee Salary Sorting (Selection Sort and Bubble Sort)
n = int(input("Enter number of employees: "))

salary = []
for i in range(n):
    s = float(input("Enter salary of employee " + str(i + 1) + ": "))
    salary.append(s)


salary1 = salary.copy()   # will be sorted using Selection Sort
salary2 = salary.copy()   # will be sorted using Bubble Sort

#Selection Sort 
for i in range(n - 1):
    small = i                     
    for j in range(i + 1, n):
        if salary1[j] < salary1[small]:
            small = j              
    
    temp = salary1[i]
    salary1[i] = salary1[small]
    salary1[small] = temp

#Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if salary2[j] > salary2[j + 1]:
        
            temp = salary2[j]
            salary2[j] = salary2[j + 1]
            salary2[j + 1] = temp


print("\nSalaries after Selection Sort:", salary1)
print("Salaries after Bubble Sort:", salary2)


print("\nTop 5 highest salaries:")
count = 0
for i in range(n - 1, -1, -1):
    if count == 5:
        break
    print(count + 1, ".", salary1[i])
    count = count + 1