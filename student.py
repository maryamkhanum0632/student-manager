students = []

while True:
    print("\n1. Add stud")
    print("2. View Students")
    print("3. Exit")
    print("4. Delete Student")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudents:")
        for student in students:
            print(student)

    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            students.remove(name)
            print("Student deleted!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

        print("Welcome from GitHub")
