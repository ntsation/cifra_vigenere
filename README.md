# Implementação da Cifra Vigenere
Este é um simples código em Python que implementa a cifra de Vigenere para criptografar e descriptografar mensagens. A cifra de Vigenere é um método clássico de criptografia que utiliza uma chave para realizar a cifragem e decifragem de textos.

## Funções
- `encrypt_vigenere` (plain_text, key): 
Esta função recebe um texto claro (plain_text) e uma chave (key) como entrada e retorna o texto criptografado usando a cifra de Vigenere.

- `decrypt_vigenere` (encrypted_text, key):
Esta função recebe um texto criptografado (encrypted_text) e uma chave (key) como entrada e retorna o texto descriptografado usando a cifra de Vigenere.

## Exemplo de Uso
- `text_to_encrypt` = "Hello, World!"

- `encryption_key` = "KEY"


### 1. Criptografar o texto
```
encrypted_text = encrypt_vigenere(text_to_encrypt, encryption_key)

print(f"Texto criptografado: {encrypted_text}")
```
### 2. Descriptografar o texto
```
decrypted_text = decrypt_vigenere(encrypted_text, encryption_key)

print(f"Texto descriptografado: {decrypted_text}")
```
Neste exemplo, o texto "Hello, World!" é criptografado com a chave "KEY" e depois descriptografado para verificar a reversibilidade do processo.

# Observações
A implementação assume que a chave e o texto claro contêm apenas caracteres alfabéticos (letras) e são case-sensitive.
Caracteres não alfabéticos no texto claro são preservados na cifragem/des cifragem.
Este código pode ser utilizado como ponto de partida para experimentação com cifras de Vigenere em projetos mais amplos de criptografia.
Sinta-se à vontade para utilizar, modificar e compartilhar conforme necessário!