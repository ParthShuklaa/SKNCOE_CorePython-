

import cryptography.fernet
from cryptography.fernet import Fernet

'''msg = input("Enter your Secret message")
key = Fernet.generate_key()
f = Fernet(key)
cipher_text = f.encrypt(msg)
print(cipher_text)
normaltext = f.decrypt(cipher_text)
print(normaltext)'''

from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b" Tony stark is alive -----A really secret message. Not for prying eyes.")
print(token)

print( f.decrypt(token))