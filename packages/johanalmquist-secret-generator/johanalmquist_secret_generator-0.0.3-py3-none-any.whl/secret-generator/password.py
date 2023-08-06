import secrets
import string
from typing import Optional


class PasswordGenerator:
    def __init__(
        self,
        letters: Optional[str] = None,
        digits: Optional[str] = None,
        special_chars: Optional[str] = "#!?@",
    ) -> None:
        """
        Args:
            letters (Optional[str], optional):  Defaults to None.
            digits (Optional[str], optional):  Defaults to None.
            special_chars (Optional[str], optional): Defaults to "#!?@".
        """
        self.letters = string.ascii_letters if not letters else letters
        self.digits = string.digits if not digits else digits
        self.special_chars = string.punctuation if not special_chars else special_chars

    def _create_secret(self, length: int) -> str:
        secret = ""
        alphabet = self.letters + self.digits + self.special_chars
        for i in range(length):
            secret += "".join(secrets.choice(alphabet))
        return secret

    def _validate(self, secret: str):
        digits_counting = 0
        special_chars_counting = 0
        for i in range(len(secret)):
            if secret[i].isdigit():
                digits_counting += 1
            elif secret[i].isalpha():
                pass
            else:
                special_chars_counting += 1

        if (
            special_chars_counting >= self.min_special_chars_value
            and digits_counting >= self.min_digits_value
        ):
            return True
        return False

    def generate(
        self,
        secret_length: int = 16,
        min_digits_value: int = 1,
        min_special_chars_value: int = 1,
    ) -> str:
        """Generate a secure password

        Args:
            secret_length (int, optional):  Defaults to 16.
            min_digits_value (int, optional): Defaults to 1.
            min_special_chars_value (int, optional): Defaults to 1.

        Returns:
            str: secure password
        """
        self.min_special_chars_value = min_special_chars_value
        self.min_digits_value = min_digits_value
        if min_digits_value is None or min_digits_value < 1:
            raise ValueError("min_digits_value must be at lest 1")

        if min_special_chars_value is None or min_special_chars_value < 1:
            raise ValueError("min_special_chars_value must be at lest 1")

        if secret_length < 8:
            raise ValueError("Secret length must be at lest 8")

        vaild = False
        secret = ""
        while not vaild:
            secret = self._create_secret(length=secret_length)
            vaild = self._validate(secret=secret)
        return secret
