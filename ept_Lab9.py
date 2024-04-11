def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str(int(digit) - 3)
        decoded_password += decoded_digit
    return decoded_password
