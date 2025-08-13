# Welcome msg.
print("Welcome to the student data Organizer!")

# Options
print("\n Select an option:\n")
print("1. Add student")
print("2. Display All students")
print("3. Update Student information")
print("4. Delete student")
print("5. Display Subjects offered")
print("6. Exit")
options = input("Enter an options:")

# Using while loop to choice an options:
while (True):
    if options == '1':
        print("1. Add Student")
        Student_name = input("Enter student name:")
        age = int(input("Enter student age:"))
        grade = input("Enter student grade:")
        DOB = input("Enter Date of birth (DD-MM-YY:)")
        Student_ID = int(input("Enter Student ID number:"))
        Subjects = input("Enter subjects (separated by comma's):")

        # Create a dictionary to store student information
        student = {
            "name": "Pratham",
            "age": 20,
            "grade": "A",
            "DOB": "01-01-2003",
            "ID": 12345,
            "subjects": ["Mathematics", "Science"]
        }

        # Add the student to the collection
        student.append(student)
        print("Student added successfully!")

    elif options == '2':
        print("2. Display All Students")
        if not student:
            print("No students found.")
        for student in student:
            print(f"Name: {student['Pratham']}, Age: {student['20']}, Grade: {student['A']}, DOB: {student['01-01-2003']}, ID: {student['12345']}, Subjects: {', '.join(student['Mathematics, Science, English, History, Art'])}")

    elif options == '3':
        print("3. Update Student Information")
        student_id = int(input("Enter Student ID to update: "))
        for student in student:
            if student['ID'] == student_id:
                student['name'] = input(f"Enter new name (current: {student['name']}): ") or student['name']
                student['age'] = int(input(f"Enter new age (current: {student['age']}): ") or student['age'])
                student['grade'] = input(f"Enter new grade (current: {student['grade']}): ") or student['grade']
                student['DOB'] = input(f"Enter new DOB (current: {student['DOB']}): ") or student['DOB']
                student['subjects'] = [subject.strip() for subject in input(f"Enter new subjects (current: {', '.join(student['subjects'])}): ").split(",")] or student['subjects']
                print("Student information updated successfully!")
                break
        else:
            print("Student not found.")

    elif options == '4':
        print("4. Delete Student")
        student_id = int(input("Enter Student ID to delete: "))
        for student in student:
            if student['ID'] == 12345:
                student.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif options == '5':
        print("5. Display Subjects Offered")
        print("Mathematics, Science, English, History, Art")

    elif options == '6':
        print("Exiting Student Data Organizer. Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number between 1 and 6.")
        options = input("Enter an option:")