from cryptography.fernet import Fernet

key = Fernet.generate_key()

fernet = Fernet(key)

with open('Private.key', 'wb') as filekey:
    filekey.write(key)

with open('Private.key', 'rb') as filekey:
    key = filekey.read()

#Reading

with open('jlhg.mp3', 'rb') as file:
    original_file = file.read()

encrypted = fernet.encrypt(original_file)

with open('encrypted_new.mp3', 'wb') as file:
    file.write(encrypted)

#Decrypted
fernet = Fernet(key)

with open('encrypted_new.mp3', 'rb') as file:
    encrypted_file = file.read()

decrypted = fernet.decrypt(encrypted_file)

with open('decrypted_new.mp3', 'wb') as file:
    file.write(decrypted)

    

