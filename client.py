import socket
import json

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

def xor_transform_text_to_bytes(text_value, key_value):
    key_value = key_value % 256
    data_bytes = text_value.encode("utf-8")
    return bytes(b ^ key_value for b in data_bytes)

def main():
    print("Enter message:")
    message_text = input().strip()
    print("Choose cipher: caesar or xor")
    cipher_choice = input().strip().lower()
    if cipher_choice == "caesar":
        print("Enter key (integer):")
        key_value = int(input().strip())
        encrypted_text = caesar_transform_text(message_text, key_value)
        payload = {"cipher": "caesar", "key": key_value, "ciphertext": encrypted_text}
        print("Message sent to server:", encrypted_text)
    elif cipher_choice == "xor":
        print("Enter key (0-255):")
        key_value = int(input().strip())
        encrypted_bytes = xor_transform_text_to_bytes(message_text, key_value)
        encrypted_text = encrypted_bytes.hex()
        payload = {"cipher": "xor", "key": key_value, "ciphertext": encrypted_text}
        print("Message sent to server:", encrypted_text)
    else:
        print("Cipher must be caesar or xor.")
        return
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 5000))
        s.sendall(json.dumps(payload).encode("utf-8"))

if __name__ == "__main__":
    main()
