import keyword
import re

# Order matters: longest operators first
operators = ["==", "!=", "<=", ">=", "//", "**", "+", "-", "*", "/", "=", "<", ">", "%"]
symbols = ["(", ")", "{", "}", "[", "]", ",", ":", ".", ";"]

# Identifier checker
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

# Number checker (int + float)
def is_number(token):
    return re.fullmatch(r'-?\d+(\.\d+)?', token) is not None

# Remove comments
def remove_comment(line):
    return line.split('#', 1)[0]

# Preserve strings
string_pattern = r'(\".*?\"|\'.*?\')'

# Read file
filename = input("Enter the Python file name (with .py extension): ").strip()

try:
    with open(filename, "r", encoding="utf-8") as file:

        tokens_list = []

        for line_number, line in enumerate(file, start=1):

            # Remove comments
            line = remove_comment(line)

            # Extract strings first
            strings = re.findall(string_pattern, line)
            line_no_strings = re.sub(string_pattern, " STRTOKEN ", line)

            # Add spacing around operators & symbols
            line_processed = line_no_strings
            for sym in operators + symbols:
                line_processed = line_processed.replace(sym, f' {sym} ')

            tokens = line_processed.split()

            str_index = 0

            for token in tokens:

                # Restore string token
                if token == "STRTOKEN":
                    real_string = strings[str_index]
                    str_index += 1
                    tokens_list.append({
                        "token": real_string,
                        "type": "STRING",
                        "line": line_number
                    })
                    continue

                # Classification
                if keyword.iskeyword(token):
                    token_type = "KEYWORD"

                elif token in operators:
                    token_type = "OPERATOR"

                elif token in symbols:
                    token_type = "SYMBOL"

                elif is_number(token):
                    token_type = "NUMBER"

                elif is_valid_identifier(token):
                    token_type = "IDENTIFIER"

                else:
                    token_type = "INVALID"

                tokens_list.append({
                    "token": token,
                    "type": token_type,
                    "line": line_number
                })

        # Output
        for t in tokens_list:
            print(f"Line {t['line']:>3}: {t['token']:<15} -> {t['type']}")

except FileNotFoundError:
    print(f"File '{filename}' not found!")
     