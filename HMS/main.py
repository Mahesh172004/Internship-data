import pymysql
from modules.patient import (
    add_patient,
    view_patients,
    update_patient,
    delete_patient
)

def main():
    while True:
        print("===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("❌ Invalid choice\n")

if __name__ == "__main__":
    main()