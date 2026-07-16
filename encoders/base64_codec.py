import base64

def encode():
    text = input("Enter text to encode: ")

    encoded = base64.b64encode(text.encode())

    print("\nEncoded Text:")
    print(encoded.decode())


def decode():
    text = input("Enter Base64 text: ")

    try:
        decoded = base64.b64decode(text.encode())

        print("\nDecoded Text:")
        print(decoded.decode())

    except:
        print("\nInvalid Base64 input!")