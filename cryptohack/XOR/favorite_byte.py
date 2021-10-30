# For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

# I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

import pwn
import Crypto.Util.number

encoded = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

for i in range(0xff):
    byte = Crypto.Util.number.long_to_bytes(i)
    try:
        string = pwn.xor(byte, bytes.fromhex(encoded)).decode('utf-8')
        if string.startswith('crypto'):
            print('Flag is: ' + string)
    except (UnicodeDecodeError, AttributeError):
        pass