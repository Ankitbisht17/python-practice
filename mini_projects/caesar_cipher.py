alphabets = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
small_alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
encd = input("Type 'encode' to encrypt, type 'decode' to decrypt:  ")
word = input("Type your message: ")
shf = int(input("Type the shift number: "))

game_over = False
while not game_over:

    def encode():
        for letter in word:

            if letter in alphabets:
                a = alphabets.index(letter)
                b = alphabets[(a + shf) % len(alphabets)]
                print(b, end="")

            elif letter in small_alphabets:
                a = small_alphabets.index(letter)
                b = small_alphabets[(a + shf) % len(small_alphabets)]
                print(b, end="")
                  

    def decode():
        for letter in word:

            if letter in alphabets:
                a = alphabets.index(letter)
                b = alphabets[(a - shf) % len(alphabets)]
                print(b, end="")

            elif letter in small_alphabets:
                a = small_alphabets.index(letter)
                b = small_alphabets[(a - shf) % len(small_alphabets)]
                print(b, end="")
            
    if encd == "encode":
        encode()
        print('')
    elif encd == "decode":
        decode()
        print('')
    game = input("Type 'Yes' if you want to continue or otherwise type 'NO' to exist. ")
    if game.lower() == "yes":
        game_over = False 
        encd = input("Type 'encode' to encrypt, type 'decode' to decrypt:  ")
        word = input("Type your message: ")
        shf = int(input("Type the shift number: "))
    elif game.lower() == 'no':
        game_over = True
    
