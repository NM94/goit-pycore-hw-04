def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Enter correct data"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Enter correct data"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Your phone  {phone}  updated"
    return f"Contact {name} not found"

def show_phone(args,contacts):
    if len(args) < 1:
        return "Enter correct data"
    name = args[0]
    return contacts.get(name, f"Contact {name} not found")

def show_all(contacts):
    if not contacts:
        return "Сontact list is empty"
    return "\n".join([f"{name}: {phone}" for name,phone in contacts.items()])



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
