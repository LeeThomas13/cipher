def encrypt(plain, shift):
    encrypted_string = ""

    for char in plain:
        num = int(char)
        shifted_num = num + shift
        shifted_num_string = str(shifted_num)
        encrypted_string += shifted_num_string

    return encrypted_string

def decrypt(encoded, shift):
    return encrypt(encoded, -shift)

