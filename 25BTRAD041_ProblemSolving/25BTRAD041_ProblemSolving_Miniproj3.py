
# Attendance Tracker

students = {}

def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
    else:
        students[name] = []
        print("Student added successfully!")

def update_attendance():
    name = input("Enter student name: ")

    if name in students:
        status = input("Enter attendance (P/A): ").upper()

        if status == "P" or status == "A":
            students[name].append(status)
            print("Attendance updated successfully!")
        else:
            print("Invalid status! Enter P or A.")
    else:
        print("Student not found!")

def display_attendance():
    if not students:
        print("No student records found.")
        return

    print("\n----- Attendance Records -----")

    for name, records in students.items():
        present = records.count("P")
        absent = records.count("A")
        total = len(records)

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("\nStudent:", name)
        print("Present:", present)
        print("Absent:", absent)
        print("Attendance Percentage:", round(percentage, 2), "%")

def check_shortage():
    threshold = float(input("Enter attendance threshold: "))

    print("\nStudents below", threshold, "% attendance:")

    for name, records in students.items():
        total = len(records)
        present = records.count("P")

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        if percentage < threshold:
            print(name, "-", round(percentage, 2), "%")

# Main Menu
while True:
    print("\n===== ATTENDANCE TRACKER =====")
    print("1. Add Student")
    print("2. Update Attendance")
    print("3. Display Attendance")
    print("4. Check Attendance Shortage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_attendance()
    elif choice == "3":
        display_attendance()
    elif choice == "4":
        check_shortage()
    elif choice == "5":
        print("Exiting Attendance Tracker...")
        break
    else:
        print("Invalid choice! Try again.")
