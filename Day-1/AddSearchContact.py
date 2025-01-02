def add_contact(name, phone, contact_list):
    contact_list[name] = phone
    return contact_list

def search_contact(name, contact_list):
    if name in contact_list:
        return contact_list[name]
    else:
        return "Contact not found"

def delete_contact(name, contact_list):
    if name in contact_list:
        del contact_list[name]
    return contact_list

contacts = {}
add_contact("John", "555-1234", contacts)
add_contact("Jane", "555-5678", contacts)
print(search_contact("John", contacts))
print(delete_contact("Jane", contacts))
print(search_contact("Jane", contacts))


# Bugs
# No check for invalid input 
# (e.g., name as an empty string or phone number format validation).
# Deleting a contact doesn’t return any feedback on success or failure.

