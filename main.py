from menu import display_menu


def main():
    print("=" * 40)
    print("      ENCODER TOOLKIT")
    print("=" * 40)

    while True:
        choice = display_menu()

        match choice:
            case "1":
                print("\n[Base64 Encode]\n")
                # TODO: Call Base64 Encode function

            case "2":
                print("\n[Base64 Decode]\n")
                # TODO: Call Base64 Decode function

            case "3":
                print("\n[Hex Encode]\n")
                # TODO: Call Hex Encode function

            case "4":
                print("\n[Hex Decode]\n")
                # TODO: Call Hex Decode function

            case "5":
                print("\n[Reverse String]\n")
                # TODO: Call Reverse String function

            case "0":
                print("\nThank you for using Encoder Toolkit.")
                break

            case _:
                print("\nInvalid option. Please try again.\n")


if __name__ == "__main__":
    main()