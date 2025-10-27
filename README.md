# Secure File Storage System (AES-256)
| Project submitted to Elevate labs by Lekha Sri G | 

🔒 SFS – Secure File Storage

Overview

SFS (Secure File Storage) is a Python-based tool designed to encrypt and decrypt files securely using either a Command-Line Interface (CLI) or a Graphical User Interface (GUI).
It allows users to store sensitive data safely by encrypting individual or multiple files into a vault, using either a password or a keyfile for protection.


---

🧩 GUI Mode

Launching the GUI

# Navigate to your project directory
cd sfs_project

# Run the GUI version of the Secure File Storage tool
python sfs_gui.py

Description

The GUI (Graphical User Interface) offers an intuitive and user-friendly layout for encryption and decryption.
Users can:

Select one or more files for encryption or decryption.

Load or generate a keyfile.

Set an output directory for encrypted or decrypted files.

Combine multiple files into a single encrypted vault.


Example Output:
The GUI window displays options such as:

> Choose File(s) → Load/Generate Keyfile → Encrypt / Decrypt




---

⚙️ CLI Mode – Encryption & Decryption

Encrypting a File

python sfs_cli.py encrypt --in-file myfile.txt --password MyStrongPass --out myfile.txt.enc

Description:
This command encrypts the file myfile.txt with the password MyStrongPass.
A new encrypted file named myfile.txt.enc will be created in the same directory.
Successful encryption is confirmed with:

> Encrypted: myfile.txt.enc




---

Advanced CLI Example (With Input & Output Directories)

# Encrypt a file and save it to an output directory
python sfs_cli.py encrypt --in-file myfile.txt --password MyStrongPass --out-dir encrypted_files/

# Decrypt the same file
python sfs_cli.py decrypt --in-file encrypted_files/myfile.txt.enc --password MyStrongPass --out-dir decrypted_files/

Description:
This advanced example shows how to specify input and output paths while encrypting and decrypting files.
It confirms successful decryption and verifies file integrity with:

> Integrity OK: True


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



---

💡 Notes

The CLI is lightweight and ideal for scripting or automation.

The GUI is user-friendly and best for manual file management.

Encrypted files use a .enc extension.

You can use either password-based or keyfile-based encryption.



---

🧠 Example Use Case

You can use SFS to securely store:

Sensitive project files

Password lists

Personal or confidential documents



---

🛠 Requirements

Python 3.x

PyQt5 or Tkinter (for GUI)

cryptography library


Install dependencies:

pip install cryptography


---

✅ Example Summary

Mode	Command	Purpose

GUI	python sfs_gui.py	Launch secure storage GUI
CLI	python sfs_cli.py encrypt ...	Encrypt files via terminal
CLI	python sfs_cli.py decrypt ...	Decrypt files via terminal



---

