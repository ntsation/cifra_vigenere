# Cifra de Vigenère

Este é um programa Python que implementa a cifra de Vigenère para criptografar e descriptografar um texto usando uma chave. A cifra de Vigenère é uma técnica de criptografia polialfabética que utiliza uma série de diferentes cifras de César com base nas letras de uma palavra-chave.

## Funcionalidades

- **criptografar(texto, chave):** Esta função recebe um texto e uma chave como entrada e retorna o texto criptografado.
- **descriptografar(texto_criptografado, chave):** Esta função recebe um texto criptografado e a chave correspondente como entrada e retorna o texto descriptografado.

## Como usar

1. Defina o texto que deseja criptografar na variável `texto`.
2. Escolha uma ou mais chaves e defina-as na lista `chave_criptografia`.
3. Execute o programa. Ele criptografará o texto usando cada chave da lista `chave_criptografia` e depois descriptografará usando as mesmas chaves em ordem reversa.
4. O texto original, o texto criptografado com cada chave e o texto descriptografado serão exibidos como saída.

## Exemplo de Uso

```python
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
```
## Resultado da Criptografia

- Texto original:
```
Um exemplo de texto para ser criptografado usando a cifra de Vigenere.
```
- Usando a chave: CRYPTO
 
    Texto criptografado:
```
Vr gkiqqnq of uukwu sxvtg vksyi fzeouigyxa nquwrk a ezbhrl enl Cwzjwdvd.
```

- Usando a chave: SEGURANCA

    Texto criptografado:
```
Zw mwqntmw sh zqjks zxmvj zpikp aizdunlqvn fsebrc w hkmmsb kof Duhycskh.
```

- Usando a chave: PROTECAO

    Texto criptografado:
```    
Sv kjtrbvrb iq rwimy jxues tmdvk ijouwyodpo czrbpt e bwqpzi dgp Ovnvzrwl.
```
