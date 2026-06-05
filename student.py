students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudents:")
        for student in students:
            print(student)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")