def encode():
    text = input("Enter text to encode: ")

    encoded = text.encode().hex()

    print("\nEncoded Text:")
    print(encoded)


def decode():
    text = input("Enter Hex text: ")

    try:
        decoded = bytes.fromhex(text)

        print("\nDecoded Text:")
        print(decoded.decode())

    except:
        print("\nInvalid Hex input!")