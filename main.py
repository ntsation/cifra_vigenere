def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')

            if char.isupper():
                encrypted_text += chr((ord(char) + key_shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + key_shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')

            if char.isupper():
                decrypted_text += chr((ord(char) - key_shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - key_shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text

# Exemplo de uso:
text_to_encrypt = "Hello, World!"
encryption_key = "N"

encrypted_text = encrypt_vigenere(text_to_encrypt, encryption_key)
print(f"Texto criptografado: {encrypted_text}")

decrypted_text = decrypt_vigenere(encrypted_text, encryption_key)
print(f"Texto descriptografado: {decrypted_text}")
