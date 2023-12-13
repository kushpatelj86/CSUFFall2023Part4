#Kush Patel
#8/30/2023
#Menu
from contacts import *
my_contacts = [["Seth", "Rune"], ["Quentin", "Miller"], ["Jack", "Malckamus"]]

print("*** TUFFY TITAN CONTACT MAIN MENU")

print("1. Print list")
print("2. Add contact")
print("3. Modify contact")
print("4. Delete contact")
print("5. Exit the program")
print()



while True:
    try:
        choice_number = int(input("Enter menu choice: "))

        if choice_number == 1:
            print_list(my_contacts)
        elif choice_number == 2:
            add_contact(my_contacts)
        elif choice_number == 3:
            modify_contact(my_contacts)
        elif choice_number == 4:
            delete_contact(my_contacts)
        elif choice_number == 5:
            break
        else:
            print("Invalid choice")
    except Exception:
            print("Invalid choice")
