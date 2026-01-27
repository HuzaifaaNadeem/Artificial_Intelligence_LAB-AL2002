def calculate_average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks)

n = int(input("Enter number of subjects: "))

marks_list = []

for i in range(n):
    mark = int(input("Enter marks: "))
    marks_list.append(mark)

average = calculate_average(marks_list)

print("Average Marks:", average)
