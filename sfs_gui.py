"""
sfs_gui.py - Minimal PyQt5 GUI for SFS project.
Requires PyQt5 installed. This GUI calls sfs_core functions.
"""
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QMessageBox, QTextEdit, QCheckBox
)
from PyQt5.QtCore import Qt
from sfs_core import encrypt_file, decrypt_file, create_vault, extract_vault, generate_random_key, save_keyfile

class SFSWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SFS - Secure File Storage")
        self.resize(600, 300)
        layout = QVBoxLayout()
        # File selection
        file_layout = QHBoxLayout()
        self.file_label = QLabel("No file selected")
        file_layout.addWidget(self.file_label)
        btn_choose = QPushButton("Choose file(s)")
        btn_choose.clicked.connect(self.choose_files)
        file_layout.addWidget(btn_choose)
        layout.addLayout(file_layout)
        # Password
        self.pw = QLineEdit()
        self.pw.setEchoMode(QLineEdit.Password)
        self.pw.setPlaceholderText("Password (leave empty to use keyfile)")
        layout.addWidget(self.pw)
        # Keyfile
        k_layout = QHBoxLayout()
        self.keyfile_label = QLabel("No keyfile")
        k_layout.addWidget(self.keyfile_label)
        btn_key = QPushButton("Load / Generate Keyfile")
        btn_key.clicked.connect(self.keyfile_action)
        k_layout.addWidget(btn_key)
        layout.addLayout(k_layout)
        # Options
        self.vault_cb = QCheckBox("Create vault from multiple files")
        layout.addWidget(self.vault_cb)
        # Output
        out_layout = QHBoxLayout()
        self.out_edit = QLineEdit()
        self.out_edit.setPlaceholderText("Output path (auto .enc for files or vault)")
        out_layout.addWidget(self.out_edit)
        btn_out = QPushButton("Browse output")
        btn_out.clicked.connect(self.choose_output)
        out_layout.addWidget(btn_out)
        layout.addLayout(out_layout)
        # Buttons
        btn_layout = QHBoxLayout()
        btn_encrypt = QPushButton("Encrypt")
        btn_encrypt.clicked.connect(self.encrypt_action)
        btn_layout.addWidget(btn_encrypt)
        btn_decrypt = QPushButton("Decrypt")
        btn_decrypt.clicked.connect(self.decrypt_action)
        btn_layout.addWidget(btn_decrypt)
        layout.addLayout(btn_layout)
        # Log
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)
        self.setLayout(layout)
        # state
        self.selected_files = []
        self.keyfile_path = None

    def log_msg(self, s):
        self.log.append(s)

    def choose_files(self):
        if self.vault_cb.isChecked():
            files, _ = QFileDialog.getOpenFileNames(self, "Select files for vault")
            if files:
                self.selected_files = files
                self.file_label.setText(f"{len(files)} file(s) selected")
        else:
            path, _ = QFileDialog.getOpenFileName(self, "Select file")
            if path:
                self.selected_files = [path]
                self.file_label.setText(os.path.basename(path))

    def choose_output(self):
        path, _ = QFileDialog.getSaveFileName(self, "Choose output file")
        if path:
            self.out_edit.setText(path)

    def keyfile_action(self):
        # Offer to load or generate a keyfile
        path, _ = QFileDialog.getSaveFileName(self, "Select keyfile path to save or cancel to load existing")
        if path:
            key = generate_random_key()
            save_keyfile(key, path)
            self.keyfile_path = path
            self.keyfile_label.setText(os.path.basename(path))
            self.log_msg(f"Generated keyfile: {path}")
        else:
            load_path, _ = QFileDialog.getOpenFileName(self, "Select keyfile to load")
            if load_path:
                self.keyfile_path = load_path
                self.keyfile_label.setText(os.path.basename(load_path))
                self.log_msg(f"Loaded keyfile: {load_path}")

    def encrypt_action(self):
        if not self.selected_files:
            QMessageBox.warning(self, "No files", "Please select file(s) first")
            return
        out_path = self.out_edit.text().strip()
        if not out_path:
            QMessageBox.warning(self, "No output", "Choose an output file")
            return
        password = self.pw.text().strip() or None
        try:
            if self.vault_cb.isChecked():
                create_vault(self.selected_files, out_path, key=None if not self.keyfile_path else None, password=password)
            else:
                encrypt_file(self.selected_files[0], out_path, key=None if not self.keyfile_path else None, password=password)
            self.log_msg(f"Encrypted to {out_path}")
            QMessageBox.information(self, "Done", "Encryption finished")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def decrypt_action(self):
        in_path, _ = QFileDialog.getOpenFileName(self, "Select .enc or vault file to decrypt")
        if not in_path:
            return
        out_dir = QFileDialog.getExistingDirectory(self, "Choose output folder")
        if not out_dir:
            return
        password = self.pw.text().strip() or None
        try:
            # We attempt vault extract first; if fails, fallback to file decrypt
            try:
                extract_vault(in_path, out_dir, key=None if not self.keyfile_path else None, password=password)
                QMessageBox.information(self, "Done", "Vault extracted")
            except Exception:
                # fallback to single-file decrypt
                decrypt_file(in_path, out_dir, key=None if not self.keyfile_path else None, password=password)
                QMessageBox.information(self, "Done", "File decrypted")
            self.log_msg(f"Decrypted/extracted to {out_dir}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SFSWindow()
    w.show()
    sys.exit(app.exec_())
