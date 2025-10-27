import os
import json
import hashlib
import base64
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def derive_key(password: bytes, salt: bytes, iterations: int = 200000) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    return kdf.derive(password)

def encrypt_file(input_path, output_path, password):
    salt = os.urandom(16)
    iv = os.urandom(12)
    key = derive_key(password.encode(), salt)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_path, "rb") as f:
        data = f.read()
    ciphertext = encryptor.update(data) + encryptor.finalize()

    tag = encryptor.tag
    metadata = {
        "filename": os.path.basename(input_path),
        "timestamp": time.time(),
        "hash": hashlib.sha256(data).hexdigest()
    }
    payload = {
        "salt": base64.b64encode(salt).decode(),
        "iv": base64.b64encode(iv).decode(),
        "tag": base64.b64encode(tag).decode(),
        "metadata": metadata,
        "ciphertext": base64.b64encode(ciphertext).decode()
    }
    with open(output_path, "w") as f:
        json.dump(payload, f)

def decrypt_file(input_path, output_dir, password):
    with open(input_path, "r") as f:
        payload = json.load(f)

    salt = base64.b64decode(payload["salt"])
    iv = base64.b64decode(payload["iv"])
    tag = base64.b64decode(payload["tag"])
    ciphertext = base64.b64decode(payload["ciphertext"])

    key = derive_key(password.encode(), salt)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    data = decryptor.update(ciphertext) + decryptor.finalize()

    filename = payload["metadata"]["filename"]
    out_path = os.path.join(output_dir, filename)
    with open(out_path, "wb") as f:
        f.write(data)

    if hashlib.sha256(data).hexdigest() != payload["metadata"]["hash"]:
        raise ValueError("Integrity check failed")

    return out_path
