# I've hidden two cool images by XOR with the same secret key so you can't see them!

import pwn

with open("/Users/blakeeriks/dev/crypto-dev/cryptohack/XOR/img/flag.png", "rb") as flag_encoded, open("/Users/blakeeriks/dev/crypto-dev/cryptohack/XOR/img/lemur.png", "rb") as lemur_encoded:
    flag = flag_encoded.read()
    lemur = lemur_encoded.read()
    flag_bytes = bytearray(flag)
    lemur_bytes = bytearray(lemur)
    
    # Solved using third party tools to xor the images together and view resulting image which contained the flag in the image