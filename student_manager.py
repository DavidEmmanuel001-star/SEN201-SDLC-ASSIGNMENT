students = []

def add_student(name, score):
    students.append({"name": name, "score": score})

def view_students():
    return students

def calculate_average():
    if len(students) == 0:
        return 0
    total = sum(student["score"] for student in students)
    return total / len(students)

def save_to_file():
    with open("data.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['score']}\n")
