
def caesar(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            shift_amount = shift if mode == "encrypt" else -shift
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        print("\nCaesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose: ")
        
        if choice in ["1", "2"]:
            text = input("Enter text: ")
            shift = int(input("Enter shift: "))
            mode = "encrypt" if choice == "1" else "decrypt"
            print(caesar(text, shift, mode))
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
