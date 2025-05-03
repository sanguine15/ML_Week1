# Task 3
student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David"
}

def search_student(roll_no):
    name = student_dict.get(roll_no)
    if name:
        print(f"Student with Roll No {roll_no}: {name}")
    else:
        print("Student not found.")

search_student(102)   
search_student(110)   