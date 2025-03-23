# 🧬 Chimera Cipher

> A polymorphic, substitution-based symmetric encryption scheme with randomized dummy insertions — designed to disrupt frequency analysis and reduce plaintext-ciphertext correlation. Inspired by the mythic beast, built for modern cryptographic research.

![License](https://img.shields.io/badge/license-MIT-green)
![Stage](https://img.shields.io/badge/stability-experimental-yellow)
![Built With Love](https://img.shields.io/badge/built%20with-love-red)

---

## 🌟 What Is Chimera?

**Chimera** is a symmetric encryption algorithm where:

- Each ASCII character is mapped to **multiple possible numeric substitutes**, chosen randomly each time it appears.
- **Dummy symbols** (random numbers not tied to any real character) are injected to confuse statistical attacks.
- The mapping (key) is **secret and non-repeating**, making it computationally hard to reverse without brute force.

This design was built with 💡 academic curiosity and cryptographic experimentation in mind — with strong resistance to classical and statistical attacks.

---

## 🔐 Why Chimera?

> Like the mythical creature — a lion, a goat, and a serpent — **Chimera Cipher** blends multiple forms into one fearsome hybrid.

- ✅ Multiple substitutions per character
- ✅ Injected randomness (dummy noise)
- ✅ Resists frequency analysis
- ✅ Reduction to NP-Hard problem (Exact Cover)
- ✅ Optional LaTeX proof + formal security definition

---

## 📖 How It Works

### 🔑 Key Generation

- Each ASCII character gets `m` unique numeric values (e.g. 8 or 16).
- All values are sampled from a large numeric space (e.g. `128–2^λ`), and **no two characters share values**.
- Additional values form a **dummy set** that adds noise.
- Output is the mapping `K`, dummy set `D`, and a PRNG seed `s`.

### 🔒 Encryption

- For each character in the plaintext, randomly select one of its assigned values from `K`.
- At random intervals (using PRNG), insert a dummy value from `D`.
- Resulting ciphertext is a mix of real + dummy numeric values.

### 🔓 Decryption

- For each ciphertext value:
  - If it belongs to a known substitution set `K(c)`, recover character `c`.
  - If it’s a dummy, ignore it.
- Reconstruct plaintext by concatenating the recovered characters.

---

## 💡 Theoretical Security

- ✅ **Resistant to frequency analysis**: Each character appears in multiple ciphertext forms.
- ✅ **NP-Hard Mapping Recovery**: We've shown that an attacker trying to recover the key (or even the real positions of characters in the ciphertext) faces a problem reducible to **Exact Cover**, which is NP-complete.
- ✅ **Provable confusion**: Dummy insertions blur ciphertext boundaries and destroy statistical patterns.

Check out the [Formal LaTeX Proof](./docs/chimera_proof.pdf) for more.

---

## 🧪 Research Status

This project is **experimental** and not production-ready. While it provides strong obfuscation and interesting theoretical properties, **it is not a replacement for modern ciphers like AES or ChaCha20** in practical deployments.

---


