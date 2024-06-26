

def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str(int(digit) - 3)
        decoded_password += decoded_digit
    return decoded_password

def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password