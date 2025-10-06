import os

doc_path = os.path.join(os.path.expanduser("~"), "Documents")

while True:
    print("\n===== Student Records Menu =====")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n=== Register Student ===")
        student_no = int(input("Student No.: "))
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        middle_initial = input("Middle Initial: ")
        program = input("Program: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        birthday = input("Birthday: ")
        contact_no = input("Contact No.: ")

        data = [
            f"Student No.: {student_no}", 
            f"Full Name: {last_name}, {first_name}, {middle_initial}",
            f"Program: {program}",
            f"Age: {age}",
            f"Gender: {gender}",
            f"Birthday: {birthday}",
            f"Contact No.: {contact_no}"
        ]
        
        file_name = f"student_no_{student_no}.txt"
        file_path = os.path.join(doc_path, file_name)

        with open(file_path, 'w') as f_p:
            for line in data:
                f_p.write(line + '\n')

        print(file_path)
        print("\nAdded Successfully!")


    elif choice == 2:
        print("\nOpen Student Record")

        student_no = input("Enter Student number: ").strip()
        file_name = f"student_no_{student_no}.txt"
        file_path = os.path.join(doc_path, file_name)
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("Student record not found.")

    else:
        print("\nExit")
        print("Thank you! Goodbye!")
        break
