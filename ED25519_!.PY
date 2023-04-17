from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import ed25519

private_key = Ed25519PrivateKey.generate()
signature = private_key.sign(b"This message is Authenticated")
public_key = private_key.public_key()
# Raises InvalidSignature if verification fails
try: public_key.verify(signature, b"This message is Authenticated"),print("Valid")
except ed25519.BadSignatureError:
    print("Signature is invalid")