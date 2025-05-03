# Task 1
marks = [
    [85, 78, 92],  
    [76, 88, 90],  
    [90, 91, 89]  
]

for i in range(3):
    total = sum(marks[i])
    average = total / len(marks[i])
    print(f"Student {i + 1} - Total: {total}, Average: {average:.2f}")
