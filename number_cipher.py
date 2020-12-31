def encrypt(plain, shift):
    encrypted_string = ""

    for char in plain:
        if char.upper() in letter_value:
            num = int(char.value)
            shifted_num = num + shift
            shifted_num_string = str(shifted_num)
            encrypted_string += shifted_num_string

        else:
            num = int(char)
            shifted_num = num + shift
            shifted_num_string = str(shifted_num)
            encrypted_string += shifted_num_string

    return encrypted_string

def decrypt(encoded, shift):
    return encrypt(encoded, -shift)

letter_value = {
    'A': '1',
    'B': '2',
    'C': '3',
    'D': '4',
    'E': '5',
    'F': '6',
    'G': '7',
    'H': '8',
    'I': '9',
    'J': '10',
    'K': '11',
    'L': '12',
    'M': '13',
    'N': '14',
    'O': '15',
    'P': '16',
    'Q': '17',
    'R': '18',
    'S': '19',
    'T': '20',
    'U': '21',
    'V': '22',
    'W': '23',
    'X': '24',
    'Y': '25',
    'Z': '26',

}

print(encrypt('zzz', 2))