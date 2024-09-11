from cryptography.fernet import Fernet

# Put this somewhere safe!

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
#print("Encrypyted token= ", token)

decrypted = f.decrypt(token)
#print("Decrypted token= ", decrypted)

