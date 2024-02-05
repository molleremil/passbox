from random import choices, shuffle, choice, randint


class PasswordGenerator():
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ".", ",", "/",
                        ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "{", "}", "|", "~"]

    def generate_password(self):

        pass_seq = []

        letters = [choice(self.letters) for _ in range(randint(5, 10))]
        numbers = [choice(self.numbers) for _ in range(randint(3, 8))]
        symbols = [choice(self.symbols) for _ in range(randint(2, 5))]

        pass_seq += letters + numbers + symbols
        shuffle(pass_seq)
        password = ''.join(pass_seq)

        return password
