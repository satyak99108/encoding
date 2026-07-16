# encoders/hex_codec.py

def encode():
    text = input("Enter text to encode: ")

    encoded = text.encode().hex()

    print("\nEncoded Text:")
    print(encoded)