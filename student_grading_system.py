import json

# Initialize an empty list to store student records
students = []

def save_record():
    with open("students_record.json", "w") as file:
        # Convert the student list to JSON and save it to a file
        json.dump(students, file)
    print("Student record saved to student_record.json")
    
def load_record():
    # Access the global student list
    global students
    try:
        with open("students_record.json", "r") as file:
            # load the student records from the file
            students = json.load(file)
        print("Student record loaded from student_record.json")
    except FileNotFoundError:
        print("No previous records found")
def add_student():
    while True:
        # .strip() removes leading and trailing whitespaces
        name = input("Name: ").strip()
        # Ensure name is not empty
        if name == "":
            print("invalid name")
        else:
            break
    while True:
        id = (input("ID: ")).strip()
        # Ensure id is not empty
        if id == "":
            print("invalid ID")
        else:
            break
    while True:
        subjects = input("How many subjects: ")
        # Ensure number of subjects is valid
        if subjects.isdigit():
            subjects = int(subjects)
            # Ensure number of subjects is positive
            if subjects > 0:
                break
        else:
            print("Invalid input")

    # List to store marks for each subject
    marks = []

    for num in range(subjects):
        while True:
            mark = input("Mark: ")
            # Ensure marks entered are valid
            if mark.isdigit():
                mark = int(mark)
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark")
            else:
                print("Invalid input")

    # Create a dictionary to store the student information
    student_record = {
        "Name": name,
        "ID": id,
        "Marks": marks
    }
    # Add the student record to the list
    students.append(student_record)
    print(f"Student {name} added")

def view_record():
    if not students:
        print("No student record found")
    else:
        for student in students:
            print(f"Name: {student['Name']}, ID: {student['ID']}, Marks: {student['Marks']}")

def calculate_grade(average):
    if average >= 85:
        return "A"
    elif 70 <= average < 85:
        return "B"
    elif 50 <= average < 70:
        return "C"
    else:
        return "F"
def calculate_grades():
    for student in students:
        name = student["Name"]
        id = student["ID"]
        marks = student["Marks"]
        average = sum(marks) / len(marks)

        # Determine the grade based on average
        grade = calculate_grade(average)

        print(f"Name: {name}, ID: {id}, Average: {average:.2f}, Grade: {grade}")

def search_student():
    while True:
        search_by = input("Search by id or name: ").strip().lower()
        if search_by not in ["id", "name"]:
            print("invalid input")
            continue
        break

    # Flag to check if student was found
    found = False
    if search_by == "id":
        search_id = input("Enter student ID: ").strip()
        for student in students:
            if search_id == student["ID"]:
                marks = student["Marks"]
                average = sum(marks) / len(marks)
                grade = calculate_grade(average)
                print(f"Name: {student['Name']}, ID: {student['ID']}, Marks: {marks}, Grade: {grade}")
                found = True
                break

    elif search_by == "name":
        search_name = input("Enter student name: ").strip().lower()
        for student in students:
            # Case insensitive search
            if search_name == student["Name"].lower():
                marks = student["Marks"]
                average = sum(marks) / len(marks)
                grade = calculate_grade(average)
                print(f"Name: {student['Name']}, ID: {student['ID']}, Marks: {marks}, Grade: {grade}")
                found = True
                break

    if not found:
        print("student not found")

def update_record():
    student_id = input("Enter student ID: ").strip()
    for student in students:
        if student_id == student["ID"]:
            # List to store updated marks
            new_marks = []
            for num in range(len(student["Marks"])):
                while True:
                    new_mark = input("Mark: ")
                    if new_mark.isdigit():
                        new_mark = int(new_mark)
                        # Ensure valid mark
                        if 0 <= new_mark <= 100:
                            new_marks.append(new_mark)
                            break
                        else:
                            print("Invalid mark")
                    else:
                        print("Invalid input")
            # Update the student's marks
            student["Marks"] = new_marks
            print(f"updated marks for {student['Name']}({student['ID']}) to {student['Marks']}")
            return
    print("Student ID not found")

def delete_record():
    student_id = input("Enter student ID: ").strip()
    for student in students:
        if student_id == student["ID"]:
            # Remove the student from the list
            students.remove(student)
            print(f"deleted {student['Name']}({student['ID']}) record")
            return
    print("Student ID not found")
def main():
    # Load existing records if available
    load_record()

    while True:
        # Display the menu options
        # "\n" to enhance visibility
        print("\n1. Add student")
        print("2. View all record")
        print("3. Calculate and display grades")
        print("4. Search student")
        print("5. Update student record")
        print("6. Delete student record")
        print("7. Save record")
        print("8. Exit")

        choice = input("Enter your choice (e.g: 1): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_record()
        elif choice == "3":
            calculate_grades()
        elif choice == "4":
            search_student()
        elif choice == "5":
            update_record()
        elif choice == "6":
            delete_record()
        elif choice == "7":
            save_record()
        elif choice == "8":
            print("Exiting program")
            break
        else:
            print("invalid choice")


main()