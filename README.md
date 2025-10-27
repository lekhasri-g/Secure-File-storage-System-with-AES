# Secure File Storage System (AES-256)

## Features
- AES-256 encryption and decryption
- Metadata storage (filename, timestamp, SHA-256 hash)
- File integrity verification

## Usage
### CLI
Encrypt a file:
```bash
python sfs_cli.py encrypt --input file.txt --password mypass
```

Decrypt a file:
```bash
python sfs_cli.py decrypt --input file.txt.enc --password mypass
```

### Dependencies
```
pip install -r requirements.txt
```
