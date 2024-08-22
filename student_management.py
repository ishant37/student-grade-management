student_grades = {}

def students_grades(name, grade):
    student_grades[name] = grade
    print(f"Student {name} has been added to the gradebook with a grade of {grade}")

def update_student(name, new_grade):
    if name in student_grades:
        student_grades[name] = new_grade
        print(f"Student {name} has been updated with a new grade of {new_grade}")
    else:
        print(f"Student {name} does not exist in the gradebook")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} has been deleted from the gradebook")
    else:
        print(f"Student {name} does not exist in the gradebook")

def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No data found")

def main():
    while True:
        print("\nGradebook Menu:")
        print("1. Add a student")
        print("2. Delete a student")
        print("3. Update a student's grade")
        print("4. Display all students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter the student's name: ")
            try:
                grade = int(input("Enter the student's grade: "))
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")
                continue
            students_grades(name, grade)

        elif choice == 2:
            name = input("Enter the student's name to delete: ")
            delete_student(name)
        elif choice == 3:
            name = input("Enter the student's name to update: ")
            try:
                grade = int(input("Enter the new grade: "))
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")
                continue
            update_student(name, grade)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Exiting the gradebook")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
