# Name: Kush Patel
# Date: 8/1/2021
# File Purpose: Lab03 main program driver program


from contacts import *

my_contacts = []

print("*** TUFFY TITAN CONTACT MAIN MENU")

print("1. Add contact")
print("2. Modify contact")
print("3. Delete contact")
print("4. Sort List")
print("5. Exit the program")
print()



while True:
    try:
        choice_number = int(input("Enter menu choice: "))

        if choice_number == 1:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            val = add_contact(my_contacts, first_name, last_name)
            if val == False:
                "Invalid Choice"
        elif choice_number == 2:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            ind = int(input("Enter index: "))
            val = modify_contact(my_contacts, first_name, last_name,ind)
            if val == False:
                "Invalid Choice"
        elif choice_number == 3:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            ind = int(input("Enter index: "))
            val = delete_contact(my_contacts)
            if val == False:
                "Invalid Choice"
        elif choice_number == 4:
            ind = int(input("Enter column index: "))
            val = sort_contacts(my_contacts)
            if val == False:
                "Invalid Choice"
        elif choice_number == 5:
            break
        else:
            print("Invalid choice")
    except Exception:
            print("Invalid choice")


