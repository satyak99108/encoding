# menu.py

def display_menu():
    """Display the main menu and return the user's choice."""

    print("\n" + "=" * 40)
    print("              MAIN MENU")
    print("=" * 40)
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. Hex Encode")
    print("4. Hex Decode")
    print("5. Reverse String")
    print("0. Exit")
    print("=" * 40)

    choice = input("Enter your choice: ").strip()
    return choice