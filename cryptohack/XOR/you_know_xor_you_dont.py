# I've encrypted the flag with my secret key, you'll never be able to guess it.

# Remember the flag format and how it might help you in this challenge!

import pwn

encoded = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

encoded_bytes = bytes.fromhex(encoded)

flag_bytes = 'crypto{'.encode()

key_part = pwn.xor(flag_bytes, encoded_bytes[:7]).decode()
key_part += 'y'

key_part = key_part * 5 + key_part[:2]
print('Flag is: ' + pwn.xor(key_part.encode(), encoded_bytes[:len(key_part)]).decode())