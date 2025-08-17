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

def xor_transform_hex_to_text(hex_string, key_value):
    key_value = key_value % 256
    data_bytes = bytes.fromhex(hex_string)
    plain_bytes = bytes(b ^ key_value for b in data_bytes)
    return plain_bytes.decode("utf-8", errors="replace")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("127.0.0.1", 5000))
        server_socket.listen(1)
        connection, address = server_socket.accept()
        with connection:
            data = connection.recv(65536)
            if not data:
                return
            payload = json.loads(data.decode("utf-8"))
            cipher_choice = payload.get("cipher", "")
            key_value = int(payload.get("key", 0))
            ciphertext_value = payload.get("ciphertext", "")
            print("Encrypted message received:", ciphertext_value)
            if cipher_choice == "caesar":
                decrypted_text = caesar_transform_text(ciphertext_value, -key_value)
                print("Decrypted message:", decrypted_text)
            elif cipher_choice == "xor":
                decrypted_text = xor_transform_hex_to_text(ciphertext_value, key_value)
                print("Decrypted message:", decrypted_text)

if __name__ == "__main__":
    main()
