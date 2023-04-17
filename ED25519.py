import ed25519

# Generate a key pair
sk, vk = ed25519.create_keypair()
print(sk,vk)

# Message to sign
message = b"This is a message"

# Sign the message
signature = sk.sign(message)

# Verify the signature using the public key
try:
    vk.verify(signature, message)
    print("Signature is valid")
except ed25519.BadSignatureError:
    print("Signature is invalid")
