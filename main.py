# Svenskt morsealfabet (A-Ö + 0–9)
morse_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    'Å': '.--.-', 'Ä': '.-.-',  'Ö': '---.',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/', '_': '_'
}

reverse_morse_dict = {v: k for k, v in morse_dict.items()}

def morse_to_text(morse):
    words = morse.strip().split(' / ')  # Dela upp ord (ord separeras med snedstreck)
    decoded_text = []

    for word in words:
        letters = word.split()
        decoded_word = ''
        for code in letters:
            decoded_word += reverse_morse_dict.get(code, '?')  # '?' om ej hittas
        decoded_text.append(decoded_word)

    return ' '.join(decoded_text)

# Exempel på användning


def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        else:
            morse_code.append('?')  # Okänd symbol
    return ' '.join(morse_code)

# Exempel på användning
text = "Det här är ett test med morsekod 1234567890 ÅÄÖ"
morse = text_to_morse(text)
print(f"flag{{{morse}}}")


text = morse_to_text(morse)
print(f"Text: {text}")
