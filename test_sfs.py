import os
import tempfile
from sfs_core import generate_random_key, save_keyfile, load_keyfile, encrypt_file, decrypt_file, create_vault, extract_vault

def test_encrypt_decrypt_roundtrip(tmp_path):
    src = tmp_path / "hello.txt"
    src.write_bytes(b"hello secure world")
    out_enc = tmp_path / "hello.txt.enc"
    # password mode
    encrypt_file(str(src), str(out_enc), password="testpass123")
    res = decrypt_file(str(out_enc), str(tmp_path), password="testpass123")
    assert res["ok"] is True
    assert (tmp_path / "hello.txt").exists()

def test_keyfile_mode(tmp_path):
    src = tmp_path / "a.bin"
    src.write_bytes(os.urandom(128))
    keypath = tmp_path / "k.key"
    key = generate_random_key()
    save_keyfile(key, str(keypath))
    out_enc = tmp_path / "a.bin.enc"
    encrypt_file(str(src), str(out_enc), key=key)
    res = decrypt_file(str(out_enc), str(tmp_path), key=key)
    assert res["ok"] is True

def test_vault(tmp_path):
    f1 = tmp_path / "f1.txt"; f1.write_text("one")
    f2 = tmp_path / "f2.txt"; f2.write_text("two")
    vault = tmp_path / "vault.enc"
    create_vault([str(f1), str(f2)], str(vault), password="vpass")
    outdir = tmp_path / "vault_out"
    outdir.mkdir()
    extract_vault(str(vault), str(outdir), password="vpass")
    assert (outdir / "f1.txt").exists()
    assert (outdir / "f2.txt").exists()
