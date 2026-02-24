marks = []
while True:
    print("***********Student Marks***********")
    print("1. Add marks")
    print("2. Display marks")
    print("3. Update marks")
    print("4. Delete marks")
    print("5.find highest marks")
    print("6. find lowest marks")
    print("7. Exit")

    choice = int(input("Enter your choice(1-7): "))

    if choice == 1:
        mark=int(input("Enter the marks of the student: "))
        marks.append(mark)
        print("Marks added successfully!")

    elif choice == 2:
        if len(marks) == 0:
            print("No marks to display.")
        else:
            print("Marks of students are:", marks)

    elif choice == 3:
        old_mark = int(input("Enter the marks to update: "))
        if old_mark in marks:
            new_mark = int(input("Enter the new marks: "))
            index = marks.index(old_mark)
            marks[index] = new_mark
            print("Marks updated successfully!")
        else:
            print("Marks not found.")

    elif choice == 4:
        mark=int(input("Enter the marks to delete: "))
        if mark in marks:
            marks.remove(mark)
            print("Marks deleted successfully!")
        else:
            print("Marks not found.")
            
    elif choice == 5:
        if len(marks) == 0:
            print("No marks to find the highest.")
        else:
            print("Highest marks are:", max(marks))
            print("Lowest marks are:", min(marks))

    elif choice == 6:
        mark=int(input("Enter the marks to find: "))
        if mark in marks:
            print("Marks found.") 
        else:            
            print("Marks not found.")

    elif choice == 7:
        print("Goodbye buddy!")
        break
    else:
        print("Invalid choice.....")