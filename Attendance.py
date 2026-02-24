users=input("enter the user id: ")
admin=input("user is present or absent(P/A): ").upper()

for i in range(7):
    if admin == "P" or admin == "A":
        print("user is present") 
        if admin == "P" :
            print("user is present for 7 days, attendance is 100%")
            break
        else: 
            print("user is absent,Not allowed to sit in the exam")
            break
    else:
        print("Invalid input. Please enter 'P' for present or 'A' for absent.")

