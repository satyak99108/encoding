# encoders/base64_codec.py

import base64

def encode():
    text = input("Enter text to encode: ")

    encoded = base64.b64encode(text.encode())

    print("\nEncoded Text:")
    print(encoded.decode())