import os

def caesar_shift_character(character, shift_value):
    if 'a' <= character <= 'z':
        base = ord('a')
        return chr((ord(character) - base + shift_value) % 26 + base)
    if 'A' <= character <= 'Z':
        base = ord('A')
        return chr((ord(character) - base + shift_value) % 26 + base)
    return character

def caesar_transform_text(text_value, shift_value):
    return ''.join(caesar_shift_character(c, shift_value) for c in text_value)

def xor_transform_bytes(byte_data, key_value):
    key_value = key_value % 256
    return bytes(b ^ key_value for b in byte_data)

def main():
    print("Choose mode: encrypt or decrypt")
    mode_choice = input("Enter mode: ").strip().lower()
    print("Choose cipher: caesar or xor")
    cipher_choice = input("Enter cipher: ").strip().lower()
    input_file_path = input("Enter path to input text file: ").strip()
    if not os.path.isfile(input_file_path):
        print("File not found. Use a full path or place the file in the same folder.")
        return
    if cipher_choice == "caesar":
        key_input = input("Enter key (integer): ").strip()
        try:
            key_value = int(key_input)
        except:
            print("Key must be an integer.")
            return
        if mode_choice == "encrypt":
            with open(input_file_path, "r", encoding="utf-8") as f:
                plain_text = f.read()
            transformed_text = caesar_transform_text(plain_text, key_value)
            output_file_path = os.path.splitext(input_file_path)[0] + ".enc"
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(transformed_text)
            print("Saved:", output_file_path)
        elif mode_choice == "decrypt":
            with open(input_file_path, "r", encoding="utf-8") as f:
                encrypted_text = f.read()
            transformed_text = caesar_transform_text(encrypted_text, -key_value)
            output_file_path = os.path.splitext(input_file_path)[0] + "_decrypted.txt"
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(transformed_text)
            print("Saved:", output_file_path)
        else:
            print("Mode must be encrypt or decrypt.")
    elif cipher_choice == "xor":
        key_input = input("Enter key (0-255): ").strip()
        try:
            key_value = int(key_input)
        except:
            print("Key must be an integer.")
            return
        if key_value < 0 or key_value > 255:
            print("Key must be between 0 and 255.")
            return
        if mode_choice == "encrypt":
            with open(input_file_path, "rb") as f:
                plain_bytes = f.read()
            transformed_bytes = xor_transform_bytes(plain_bytes, key_value)
            output_file_path = os.path.splitext(input_file_path)[0] + ".enc"
            with open(output_file_path, "wb") as f:
                f.write(transformed_bytes)
            print("Saved:", output_file_path)
        elif mode_choice == "decrypt":
            with open(input_file_path, "rb") as f:
                encrypted_bytes = f.read()
            transformed_bytes = xor_transform_bytes(encrypted_bytes, key_value)
            output_file_path = os.path.splitext(input_file_path)[0] + "_decrypted.txt"
            with open(output_file_path, "wb") as f:
                f.write(transformed_bytes)
            print("Saved:", output_file_path)
        else:
            print("Mode must be encrypt or decrypt.")
    else:
        print("Cipher must be caesar or xor.")

if __name__ == "__main__":
    main()
