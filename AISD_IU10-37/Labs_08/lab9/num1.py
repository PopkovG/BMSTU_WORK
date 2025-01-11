import random
from sympy import mod_inverse

# --- Шифр Виженера ---
def generate_vigenere_key(message, user_key):
    """Генерация ключа для шифра Виженера на основе пользовательского ключа."""
    filtered_key = ''.join(filter(str.isalpha, user_key)).upper()
    if not filtered_key:
        raise ValueError("Ключ должен содержать хотя бы одну букву.")

    repeated_key = (filtered_key * ((len(message) // len(filtered_key)) + 1))[:len(message)]
    return repeated_key

def vigenere_encrypt(message, user_key):
    key = generate_vigenere_key(message, user_key)
    encrypted = []
    for m, k in zip(message, key):
        if m.isalpha():
            offset = 65 if m.isupper() else 97
            encrypted.append(chr((ord(m) - offset + (ord(k.upper()) - 65)) % 26 + offset))
        else:
            encrypted.append(m)
    return ''.join(encrypted)

def vigenere_decrypt(encrypted_message, user_key):
    key = generate_vigenere_key(encrypted_message, user_key)
    decrypted = []
    for c, k in zip(encrypted_message, key):
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            decrypted.append(chr((ord(c) - offset - (ord(k.upper()) - 65)) % 26 + offset))
        else:
            decrypted.append(c)
    return ''.join(decrypted)

# --- Криптосистема Пэйе ---
def generate_paillier_key():
    """Генерация ключей для криптосистемы Пэйе."""
    p = random.choice([11, 13, 17, 19, 23])  # Простые числа
    q = random.choice([29, 31, 37, 41, 43])
    n = p * q
    g = n + 1
    lambda_val = (p - 1) * (q - 1)
    mu = mod_inverse(lambda_val, n)
    return (n, g), (lambda_val, mu)


def paillier_encrypt(message, public_key):
    """Шифрование числа в криптосистеме Пэйе."""
    n, g = public_key
    n_sq = n ** 2
    m = int.from_bytes(message.encode(), 'big')  # Перевод строки в число
    r = random.randint(1, n - 1)
    c = (pow(g, m, n_sq) * pow(r, n, n_sq)) % n_sq
    return c

def paillier_decrypt(ciphertext, private_key, public_key):
    """Дешифрование числа в криптосистеме Пэйе."""
    lambda_val, mu = private_key
    n, _ = public_key
    n_sq = n ** 2
    l = (pow(ciphertext, lambda_val, n_sq) - 1) // n
    m = (l * mu) % n
    return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()

# --- Основная программа ---
if __name__ == "__main__":
    user_key = "фф12К52"
    message = "Hello, World!"

    # Шифрование и дешифрование с использованием шифра Виженера
    vigenere_encrypted = vigenere_encrypt(message, user_key)
    vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, user_key)
    print("Виженер шифрование: ", vigenere_encrypted)
    print("Виженер дешифрование: ", vigenere_decrypted)

    # Генерация ключей для криптосистемы Пэйе
    public_key, private_key = generate_paillier_key()

    # Шифрование и дешифрование с использованием криптосистемы Пэйе
    paillier_encrypted = paillier_encrypt(message, public_key)
    paillier_decrypted = paillier_decrypt(paillier_encrypted, private_key, public_key)
    print("Пэйе шифрование: ", paillier_encrypted)
    print("Пэйе дешифрование: ", paillier_decrypted)
