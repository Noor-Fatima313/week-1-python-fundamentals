import json
import os

file_name = "students.json"


# Load students from file
def load_students():
    if os.path.exists(file_name):

        try:
            file = open(file_name, "r")
            students = json.load(file)
            file.close()
            return students

        except:
            return []

    return []


# Save students into file
def save_students():

    file = open(file_name, "w")
    json.dump(student_list, file, indent=4)
    file.close()


# Add student
def add_student():

    print("\nADD STUDENT")

    student_id = input("Enter ID: ")

    # Check duplicate ID
    for student in student_list:
        if student["id"] == student_id:
            print("ID already exists.")
            return

    name = input("Enter Name: ")

    try:
        age = int(input("Enter Age: "))
    except:
        print("Age must be a number.")
        return

    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    student_list.append(student)

    save_students()

    print("Student added successfully.")


# View students
def view_students():

    print("\nALL STUDENTS")

    if len(student_list) == 0:
        print("No records found.")
        return

    for student in student_list:

        print("---------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


# Search by ID
def search_student():

    student_id = input("Enter Student ID: ")

    for student in student_list:

        if student["id"] == student_id:

            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

            return

    print("Student not found.")


# Search by name (Bonus)
def search_by_name():

    name = input("Enter Name: ").lower()

    found = False

    for student in student_list:

        if student["name"].lower() == name:

            print("---------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

            found = True

    if found == False:
        print("Student not found.")


# Update student
def update_student():

    student_id = input("Enter Student ID: ")

    for student in student_list:

        if student["id"] == student_id:

            print("Leave blank if no change.")

            new_name = input("New Name: ")
            new_age = input("New Age: ")
            new_course = input("New Course: ")

            if new_name != "":
                student["name"] = new_name

            if new_course != "":
                student["course"] = new_course

            if new_age != "":
                try:
                    student["age"] = int(new_age)
                except:
                    print("Invalid age.")

            save_students()

            print("Student updated successfully.")
            return

    print("Student not found.")


# Delete student
def delete_student():

    student_id = input("Enter Student ID: ")

    for student in student_list:

        if student["id"] == student_id:

            student_list.remove(student)

            save_students()

            print("Student deleted successfully.")
            return

    print("Student not found.")


# Statistics (Bonus)
def student_statistics():

    print("\nSTATISTICS")
    print("Total Students:", len(student_list))


# Main menu
def menu():

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by ID")
        print("4. Search Student by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Student Statistics")
        print("8. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            search_by_name()

        elif choice == "5":
            update_student()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            student_statistics()

        elif choice == "8":
            print("Program Closed.")
            break

        else:
            print("Invalid Choice.")


student_list = load_students()

menu()
