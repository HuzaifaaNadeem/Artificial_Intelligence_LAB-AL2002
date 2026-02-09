print("Smart Classroom Light Controller\n")

studentPresence = ["No", "Yes", "Yes", "No", "No", "Yes", "Yes", "No"]

previousStudents = "No"
previousLight = "OFF"
currentLight = "OFF"

for step in range(8):
    students = studentPresence[step]

    if students == "Yes" and currentLight == "OFF":
        action = "Turning lights ON"
        currentLight = "ON"
    elif students == "No" and currentLight == "ON":
        action = "Turning lights OFF"
        currentLight = "OFF"
    else:
        action = "No action needed"

    print(f"Step {step + 1}")
    print(f"Students Present: {students}")
    print(f"Action Taken: {action}")
    print(f"Agent Memory → Previous Students: {previousStudents}, Previous Light: {previousLight}")
    print("-" * 45)

    previousStudents = students
    previousLight = currentLight
