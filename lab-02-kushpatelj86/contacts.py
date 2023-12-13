#Kush Patel
#8/30/2023
#List of contacts
def print_list(contacts):
    """This will print every contact in the list"""
    print("================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")

    for i in range(len(contacts)):
        if len(contacts[i]) == 2:
            print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

          





def add_contact(contacts):
    """This will add a new contact"""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name : ")
    contacts.append([first_name, last_name])
    return contacts



def modify_contact(contact_list):
        """This will modify a new contact"""
        try:
             
            contact_number = int(input("Enter index number: "))

            if contact_number >= 0 or contact_number < len(contact_list):
                
                first_name = input("Enter first name: ")
                last_name = input("Enter last name : ")
                contact_list[contact_number] = ([first_name, last_name])
                return contact_list


        except Exception:
            print("Invalid index number.")
            return contact_list



def delete_contact(contact_list):
    try:
        """This will delete the contact"""
        contact_number = int(input("Enter index number: "))
        if contact_number >= 0 or contact_number < len(contact_list):
            contact_list.remove(contact_list[contact_number])
            return contact_list
    except Exception:         
         print("Invalid index number.")
         return contact_list

