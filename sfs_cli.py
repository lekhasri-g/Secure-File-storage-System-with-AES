import argparse
from sfs_core import encrypt_file, decrypt_file

def main():
    parser = argparse.ArgumentParser(description="Secure File Storage System with AES-256")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=False, help="Output file path or directory")
    parser.add_argument("--password", required=True, help="Password for encryption/decryption")
    args = parser.parse_args()

    if args.mode == "encrypt":
        output = args.output or args.input + ".enc"
        encrypt_file(args.input, output, args.password)
        print(f"Encrypted file saved as: {output}")
    else:
        output_dir = args.output or "."
        path = decrypt_file(args.input, output_dir, args.password)
        print(f"Decrypted file saved as: {path}")

if __name__ == "__main__":
    main()
