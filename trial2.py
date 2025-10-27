student_name = input("Enter the student's name: ")

num_subjects = int(input("Enter the number of subjects: "))

subjects = []

for i in range(num_subjects):
    subject = input(f"Enter name of subject {i+1}: ")
    subjects.append(subject)

print("\n--- Student Information ---")
print(f"Name: {student_name}")
print("Subjects Enrolled:")
for subject in subjects:
    print(f"- {subject}")
