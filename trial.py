num_subjects = int(input("Enter number of subjects this semester: "))
subjects = []

for i in range(num_subjects):
    subject = input(f"Enter name of subject {i + 1}: ")
    subjects.append(subject)


print("\nYour subjects this semester are:")
for i, subject in enumerate(subjects, 1):
    print(f"{i}. {subject}")
