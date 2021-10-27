# Now you've got the hang of the various encodings you'll be encountering, let's have a look at automating it.

# Can you pass all 100 levels to get the flag?

# The 13377.py file attached below is the source code for what's running on the server. The pwntools_example.py file provides the start of a solution using the incredibly convenient pwntools library. which we recommend. If you'd prefer to use Python's in-built telnetlib, telnetlib_example.py is also provided.

# For more information about connecting to interactive challenges, see the FAQ. Feel free to skip ahead to the cryptography if you aren't in the mood for a coding challenge!

# Connect at nc socket.cryptohack.org 13377

import pwn # pip install pwntools
import codecs
import json
import base64
import Crypto.Util.number

r = pwn.remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:

    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    if 'flag' in received:
        print(received['flag'])
        break

    encoded = received["encoded"]
    type = received["type"]

    decoded = ''
    if type == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif type == "base64":
        decoded = base64.b64decode(encoded).decode('utf-8')
    elif type == "hex":
        decoded = bytes.fromhex(encoded).decode('utf-8')
    elif type == "bigint":
        temp = int(encoded, 16)
        decoded = Crypto.Util.number.long_to_bytes(temp).decode('utf-8')
    elif type == "utf-8":
        decoded = ''.join([chr(b) for b in encoded])

    to_send = {
    "decoded": decoded
    }
    print("Sending: " + str(decoded))
    json_send(to_send)
