student = {}

print("\n*****Student Grade Management*****")
print("\n***Main Menu***\n")
print("   1. Add Student")
print("   2. Add Grade")
print("   3. View Students & Grade")
print("   4. Exit")

while True:

    choice = input("\nSelect a from menu (1 - 4)\nEnter: ")

    if choice == "1":
        name = input("\nInput a student:\nEnter: ")
        if name in student:
            print("\nStudent Already Exist!")
        else:
            student[name] = []
            print("\nStudent Added!")

    elif choice == "2":
        name = input("\nEnter the name of student:\nEnter: ")
        grade = float(input("\nInput a Grade:\nEnter: "))
        if name not in student:
            print("\nStudent Doesn't Exist!")
        else:
            student[name].append(name)
            print("\nGrade Added!")

    elif choice == "3":
        if not name in student:
            print("\nStudent Doesn't Exist!")
        else:
            for name in student:
                print(name, ":", student[name])
    elif choice == "4":
        print("\n*****Thank you*****")

    else:
        print("*****Error*****")
