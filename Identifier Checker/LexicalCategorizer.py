import keyword

# Function to check if a string is a valid identifier
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

# Predefined lists of keywords and operators
custom_keywords = ["if", "else", "while", "int", "float"]
operators = ["+", "-", "=", "*", "/", "=="]

# Take a line of code as input
sentence = input("Enter a line of code: ").strip()

# Split the line into words/tokens
tokens = sentence.split()

# Analyze each token
for word in tokens:
    if keyword.iskeyword(word):
        print(word, "is a KEYWORD")
    elif word in operators:
        print(word, "is an OPERATOR")
    elif is_valid_identifier(word):
        print(word, "is an IDENTIFIER")
    else:
        print(word, "is INVALID")