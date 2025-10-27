# 🔐 Secure File Storage System (AES-256)

A **secure local file encryption and storage application** built in Python using **AES-256-GCM** encryption.  
It provides both a **Command-Line Interface (CLI)** and an optional **PyQt5 graphical interface** to safely encrypt, decrypt, and verify files.

---

## 🚀 Features

- **AES-256-GCM encryption** for strong confidentiality and integrity  
- **Password-based key derivation (PBKDF2-HMAC-SHA256)**  
- **Automatic metadata storage** (file name, timestamp, SHA-256 hash)  
- **Integrity verification** to detect tampering  
- **Vault-style encrypted storage** (optional)  
- **Simple CLI & PyQt5 GUI interface**

---

## 🧩 Project Structure

sfs_project/
├── sfs_core.py # Core AES encryption/decryption logic
├── sfs_cli.py # Command-line interface
├── sfs_gui.py # (Optional) PyQt5 GUI for file operations
├── requirements.txt # Project dependencies
├── tests/ # Unit tests for encryption/decryption
│ └── test_sfs.py
├── README.md # Project documentation
└── LICENSE # MIT License

yaml
Copy code

---

## ⚙️ Installation

1. **Clone or extract the project**
   ```bash
   unzip sfs_project.zip -d sfs_project
   cd sfs_project
Install dependencies

bash
Copy code
python -m pip install -r requirements.txt
🧰 Usage (CLI)
🔒 Encrypt a file
bash
Copy code
python sfs_cli.py encrypt --input myfile.txt --password MyStrongPass
Output:
myfile.txt.enc → Encrypted file (includes metadata and hash)

🔓 Decrypt a file
bash
Copy code
python sfs_cli.py decrypt --input myfile.txt.enc --password MyStrongPass
Output:
myfile.txt → Original restored file (integrity verified)

🖥️ Usage (GUI)
If you prefer a graphical interface:

bash
Copy code
python sfs_gui.py
You can then browse, encrypt, and decrypt files through a simple PyQt5 window.

🧠 Security Details
Algorithm: AES-256 in GCM mode

Key Derivation: PBKDF2-HMAC-SHA256 with 200,000 iterations

Integrity Check: SHA-256 file hash + AES-GCM authentication tag

Salt & IV: Randomly generated per file

Metadata: Encrypted JSON (filename, timestamp, SHA-256 hash)

🧪 Testing
To verify the system:

bash
Copy code
pytest tests/
This ensures encryption and decryption functions correctly and integrity checks are validated.

📜 License
This project is released under the MIT License.
You are free to use, modify, and distribute it, provided proper credit is given.

👨‍💻 Author
Developed by: LEKHA SRI G
Year: 2025
Tech Stack: Python, Cryptography, PyQt5

💡 Future Enhancements
Secure vault mode with multi-file encryption

Key management and password strength validation

Encrypted metadata index for quick search

GUI improvements (progress bars, drag-and-drop)

⚠️ Disclaimer: This project is for educational and local file-security purposes only.
It should not be used for commercial or military-grade encryption without additional review.
