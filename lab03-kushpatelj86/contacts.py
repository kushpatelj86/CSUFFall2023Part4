#Kush Patel
#8/30/2023
#List of contacts


def add_contact(contact_list, first_name="James",last_name="Wiegman"):
        contact_list.append([first_name,last_name])



def modify_contact(contact_list, first_name="Ethan",last_name="Avalos",index=0):
            if index >=0 and index < len(contact_list):  
                contact_list[index] = [first_name,last_name]
                return True
            else:
               return False



def delete_contact(contact_list, first_name="Logan",last_name="Porras",index=0):
            if index >=0 and index < len(contact_list):  
                del contact_list[index]
                return True
            else:
               return False



def sort_contacts(contact_list, column=0):
    try:
        if column == 0 or column == 1:
            contact_list.sort(key = lambda x : x[column])
    except Exception:
            contact_list


