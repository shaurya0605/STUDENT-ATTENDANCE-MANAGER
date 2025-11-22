attendance = []

def add_student():
    name=input("Student name: ")
    status= input("Present or Absent: ")
    attendance.append({"name": name, "status": status})
    print("Entry added!")

def view_attendance():
    if not attendance:
        print("No records yet.")
        return

    print(" Attendance Records ")
    for i, info in enumerate(attendance, 1):
        print(str(i) + ". " + info["name"] + " - " + info["status"])

def total_summary():
    present = 0
    absent = 0

    for s in attendance:
        if s["status"].lower() == "present":
            present += 1
        elif s["status"].lower() == "absent":
            absent += 1

    print("Total Present: "+ str(present))
    print("Total Absent: "+ str(absent))

while True:
    print("\n1. Add Attendance")
    print("2. View Attendance")
    print("3. Summary")
    print("4. Exit")

    choice=input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        total_summary()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice")