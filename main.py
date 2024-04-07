def criptografar(texto, chave):
    texto_criptografado = ""
    tamanho_chave = len(chave)

    for i in range(len(texto)):
        caractere = texto[i]
        if caractere.isalpha():
            caractere_chave = chave[i % tamanho_chave]
            deslocamento_chave = ord(caractere_chave.upper()) - ord('A')

            if caractere.isupper():
                texto_criptografado += chr((ord(caractere) + deslocamento_chave - ord('A')) % 26 + ord('A'))
            else:
                texto_criptografado += chr((ord(caractere) + deslocamento_chave - ord('a')) % 26 + ord('a'))
        else:
            texto_criptografado += caractere

    return texto_criptografado

def descriptografar(texto_criptografado, chave):
    texto_descriptografado = ""
    tamanho_chave = len(chave)

    for i in range(len(texto_criptografado)):
        caractere = texto_criptografado[i]
        if caractere.isalpha():
            caractere_chave = chave[i % tamanho_chave]
            deslocamento_chave = ord(caractere_chave.upper()) - ord('A')

            if caractere.isupper():
                texto_descriptografado += chr((ord(caractere) - deslocamento_chave - ord('A')) % 26 + ord('A'))
            else:
                texto_descriptografado += chr((ord(caractere) - deslocamento_chave - ord('a')) % 26 + ord('a'))
        else:
            texto_descriptografado += caractere

    return texto_descriptografado

# Exemplo de uso:
texto = "Um exemplo de texto para ser criptografado usando a cifra de Vigenere."
chave_criptografia = ["CRYPTO", "SEGURANCA", "PROTECAO"]

print("Texto original:")
print(texto)

texto_criptografado = texto

for chave in chave_criptografia:
    texto_criptografado = criptografar(texto_criptografado, chave)
    print("\nUsando a chave:", chave)
    print("Texto criptografado:")
    print(texto_criptografado)

texto_descriptografado = texto_criptografado

for chave in reversed(chave_criptografia):
    texto_descriptografado = descriptografar(texto_descriptografado, chave)

print("\nTexto descriptografado:")
print(texto_descriptografado)
