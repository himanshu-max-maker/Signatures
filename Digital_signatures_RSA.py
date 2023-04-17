from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

key = RSA.generate(2048)

# Get the private and public keys
private_key = key.export_key()
public_key = key.publickey().export_key()

message = b"Message will be signed "

                                    #Hash the message
hash = SHA256.new(message)

signature = pkcs1_15.new(RSA.import_key(private_key)).sign(hash)  # Signing the massage using private key and hash
print(signature)

# Verify the signature with the public key
if pkcs1_15.new(RSA.import_key(public_key)).verify(hash, signature):
    print("The signature is valid.")
else:
    print("The signature is not valid.")
