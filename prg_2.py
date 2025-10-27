subjects = []
n = int(input("Enter the number of subjects: "))
for i in range(n):
    subject = input(f"Enter the name of subject {i+1}: ")
    subjects.append(subject)
print("\nThe subjects you entered are:")
for subject in subjects:
    print(subject)