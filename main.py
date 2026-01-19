from student_manager import add_student, view_students, calculate_average, save_to_file

while True:
    print("\nStudent Score Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        score = float(input("Enter score: "))
        add_student(name, score)
        print("Student added successfully.")

    elif choice == "2":
        students = view_students()
        for student in students:
            print(student["name"], "-", student["score"])

    elif choice == "3":
        avg = calculate_average()
        print("Average Score:", avg)

    elif choice == "4":
        save_to_file()
        print("Data saved. Exiting...")
        break

    else:
        print("Invalid choice.")
