# chimera_cipher.py

import random
from typing import Dict, List, Tuple

class ChimeraCipher:
    def __init__(self, substitutions_per_char: int = 8, dummy_range: Tuple[int, int] = (128, 2048)):
        self.ascii_chars = [chr(i) for i in range(128)]
        self.subs_per_char = substitutions_per_char
        self.dummy_start, self.dummy_end = dummy_range
        self.key_map: Dict[str, List[int]] = {}
        self.dummy_set: set = set()
        self._generate_key()

    def _generate_key(self) -> None:
        total_subs = len(self.ascii_chars) * self.subs_per_char
        all_candidates = list(range(self.dummy_start, self.dummy_end))
        keyspace = random.sample(all_candidates, total_subs)

        self.key_map = {
            char: keyspace[i * self.subs_per_char : (i + 1) * self.subs_per_char]
            for i, char in enumerate(self.ascii_chars)
        }

        used_values = set(v for subs in self.key_map.values() for v in subs)
        self.dummy_set = set(all_candidates) - used_values

    def encrypt(self, message: str) -> List[int]:
        ciphertext = []
        for ch in message:
            if ch not in self.key_map:
                raise ValueError(f"Character '{ch}' not in ASCII set.")
            real_val = random.choice(self.key_map[ch])
            ciphertext.append(real_val)
            # Insert one dummy after each character
            dummy_val = random.choice(list(self.dummy_set))
            ciphertext.append(dummy_val)
        return ciphertext

    def decrypt(self, ciphertext: List[int]) -> str:
        reverse_map = {}
        for char, values in self.key_map.items():
            for val in values:
                reverse_map[val] = char

        plaintext = []
        for val in ciphertext:
            if val in reverse_map:
                plaintext.append(reverse_map[val])
        return ''.join(plaintext)

    def get_key(self) -> Dict[str, List[int]]:
        return self.key_map


if __name__ == "__main__":
    cipher = ChimeraCipher()
    message = input("Enter your message: ")
    ciphertext = cipher.encrypt(message)
    print("Ciphertext:", ciphertext)

    decrypted = cipher.decrypt(ciphertext)
    print("Decrypted:", decrypted)
