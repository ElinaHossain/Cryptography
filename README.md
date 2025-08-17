# Cryptography

Project Name: Encryption Tool
Files:
1) encrypt_tool.py
2) client.py
3) server.py
4) sample.txt
5) sample.enc
6) sample_decrypted.txt
7) README.txt

How to run:
1) Put your input file in the same folder or use a full path.
2) Run: python encrypt_tool.py
3) When asked:
   - Enter mode: encrypt or decrypt
   - Enter cipher: caesar or xor
   - Enter key: integer for caesar, 0-255 for xor
   - Enter the path to your input file
4) The tool saves .enc for encrypt and _decrypted.txt for decrypt in the same folder.

Examples:
Encrypt Caesar:
Enter mode: encrypt
Enter cipher: caesar
Enter key: 3
Enter path to input text file: sample.txt
Output: sample.enc

Decrypt Caesar:
Enter mode: decrypt
Enter cipher: caesar
Enter key: 3
Enter path to input text file: sample.enc
Output: sample_decrypted.txt

Encrypt XOR:
Enter mode: encrypt
Enter cipher: xor
Enter key: 5
Enter path to input text file: sample.txt
Output: sample.enc

Decrypt XOR:
Enter mode: decrypt
Enter cipher: xor
Enter key: 5
Enter path to input text file: sample.enc
Output: sample_decrypted.txt

How to run the sockets:
Open two terminals in the same folder.

Terminal 1 (server):
python server.py

Terminal 2 (client):
python client.py
Enter message: Hello
Choose cipher: Caesar or xor
Enter key: matching key
Client prints the sent encrypted message.
Server prints the encrypted message received and the decrypted message.
