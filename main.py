print('''
  __  __                                          _           
 |  \/  |___ _ _ ___ ___   __ ___ _ ___ _____ _ _| |_ ___ _ _ 
 | |\/| / _ \ '_(_-</ -_) / _/ _ \ ' \ V / -_) ' \  _/ -_) '_|
 |_|  |_\___/_| /__/\___| \__\___/_||_\_/\___|_||_\__\___|_|  
                                                              
''')
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '!': '-.-.--', '/': '-..-.',
                   '-': '-....-', "'": '.----.', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-',
                   '+': '.-.-.', '_': '..--.-', '"': '.-..-.',
                   '$': '...-..-', '@': '.--.-.', '¿': '..-.-',
                   '¡': '--...-', '(': '-.--.', ')': '-.--.-'}

msg = input("write Your message to covert to morse code(only A-Z letters and 0-9 numbers or"
            " '.,?'!/()&:;=+-_\"$@' '#' is used for unknown character and should be ignored:\n").upper()


#### V2 ####
def morse_converter(message):
    converted_string = ""
    for char in message:
        if char == ' ':
            converted_string += '/ '
        else:
            try:
                converted_string += MORSE_CODE_DICT[char] + ' '
            except KeyError:
                converted_string += '# '
    print(converted_string)


morse_converter(msg)


#### V1 ####
# letters_table = []
# converted_string = ""
# words = msg.split()
#
# for word in words:
#     letters = list(word)
#     letters_table.append(letters)
#
# for word in letters_table:
#     for letter in word:
#         try:
#             converted_string += MORSE_CODE_DICT[letter] + ' '
#         except KeyError:
#             converted_string += '# '
#     if word != letters_table[-1]:
#         converted_string += '/ '
#
# print(converted_string)