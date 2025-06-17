def caesar_shift(message, shift):
     
    result = ""

    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code >90:
                new_char_code -= 26

            elif new_char_code < 65:
                new_char_code += 26

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char
                
    print(result)

user_message = input("Enter the text Encrypt:")
shift_key =int(input("Enter the shift key:"))

caesar_shift(user_message, shift_key)


