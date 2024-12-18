import secrets
import string
import re

class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True):
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # Get characters from string module
        self.base_characters: str = string.ascii_lowercase + string.digits

        if self.use_uppercase is True:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols is True:
            self.base_characters += string.punctuation

    def generate(self) -> str:
        password: list [str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))
        return ''.join(password)

    @staticmethod
    def is_strong(password: str) -> bool:
        if len(password) < 16:
             return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

def main() -> None:
    password: Password = Password(length=25, symbols=False)
    generated: str = password.generate()

    if Password.is_strong(generated):
        print("The password is strong enough")
    else:
        print("The password is weak")



if __name__ == '__main__':
    main()




