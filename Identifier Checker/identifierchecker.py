import keyword

def is_valid_identifier(identifier):
    if not identifier:
        return False
    if keyword.iskeyword(identifier):
        return False
    if not (identifier[0].isalpha() or identifier[0] == '_'):
        return False
    for char in identifier[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    return True

# Main loop to take user input
while True:
    user_input = input("Enter an identifier to check (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("Exiting...")
        break

    if is_valid_identifier(user_input):
        print(f"'{user_input}' is a VALID identifier.")
    else:
        print(f"'{user_input}' is an INVALID identifier.")