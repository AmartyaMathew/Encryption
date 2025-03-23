# Formal Description of the Encryption Algorithm

---

## **1. Notation**
- **Message Space**:  
  \( \mathcal{M} = \{ m \mid m \text{ is a sequence of ASCII characters } (0 \leq \text{ord}(c) \leq 127) \} \).
- **Ciphertext Space**:  
  \( \mathcal{C} = \text{sequence of integers } \subseteq \mathbb{N} \).
- **Keys**:  
  - \( K_{\text{msg}} \): Master substitution key (e.g., 256-bit secret).  
  - \( K_{\text{rnd}} \): Master randomness key (e.g., 256-bit secret).  
- **Nonce**:  
  \( N \in \{0, 1\}^{128} \), a unique public value per encryption.  
- **Hash Function**:  
  \( H: \{0, 1\}^* \to \{0, 1\}^{64} \), modeled as a random oracle.  
- **Parameters**:  
  - \( \ell_{\text{noise}} = \lfloor \alpha \cdot |m| \rfloor \), where \( \alpha \in [0, 1] \).  

---

## **2. Key Generation**  
\[ (K_{\text{msg}}, K_{\text{rnd}}) \leftarrow \text{KeyGen}(1^\lambda) \]  
- **Input**: Security parameter \( \lambda \).  
- **Output**: Two keys sampled uniformly at random:  
  \[ K_{\text{msg}} \leftarrow \{0, 1\}^\lambda, \quad K_{\text{rnd}} \leftarrow \{0, 1\}^\lambda. \]

---

## **3. Encryption**  
\[ C \leftarrow \text{Enc}(K_{\text{msg}}, K_{\text{rnd}}, N, m) \]  
**Input**:  
- Plaintext \( m = c_1 c_2 \dots c_n \), where \( c_i \in \mathcal{M} \).  
- Nonce \( N \).  

**Steps**:  
1. **Substitute Characters**:  
   For each \( c_i \):  
   \[ s_i = H(K_{\text{msg}} \parallel N \parallel c_i) \mod 2^{64}. \]  
2. **Generate Noise**:  
   For \( j = 1, \dots, \ell_{\text{noise}} \):  
   \[ r_j = H(K_{\text{rnd}} \parallel N \parallel j) \mod 2^{64}. \]  
3. **Construct Ciphertext**:  
   Interleave substitutes and noise, then shuffle:  
   \[ C = \text{Permute}([s_1, \dots, s_n, r_1, \dots, r_{\ell_{\text{noise}}}]). \]  

**Output**: Ciphertext \( C \).  

---

## **4. Decryption**  
\[ m \leftarrow \text{Dec}(K_{\text{msg}}, N, C) \]  
**Input**:  
- Ciphertext \( C \).  

**Steps**:  
1. **Recompute Substitutes**:  
   For every ASCII value \( c \in \{0, \dots, 127\} \):  
   \[ s_c = H(K_{\text{msg}} \parallel N \parallel c) \mod 2^{64}. \]  
   Collect substitutes in \( \mathcal{S} = \{s_c \mid c \in \{0, \dots, 127\}\} \).  
2. **Filter Ciphertext**:  
   Extract substitutes:  
   \[ \{\hat{s}_1, \dots, \hat{s}_n\} = \{x \in C \mid x \in \mathcal{S}\}. \]  
3. **Recover Plaintext**:  
   For each \( \hat{s}_i \), find \( c_i \) where \( s_{c_i} = \hat{s}_i \).  

**Output**: Plaintext \( m = c_1 c_2 \dots c_n \).  

---

## **5. Security Arguments**  
1. **Indistinguishability**:  
   - Substitutes \( s_i \) and noise \( r_j \) are indistinguishable under the random oracle model.  
   - Adversaries cannot link \( s_i \) to \( c_i \) without \( K_{\text{msg}} \).  
2. **Nonce Uniqueness**:  
   - Ensures fresh substitutes/noise per encryption, preventing key reuse attacks.  
3. **Reduction to NP-Hardness**:  
   - Recovering \( K_{\text{msg}} \) reduces to solving the **Exact Cover problem** (partitioning observed substitutes into 128 subsets of size 8).  
   - Noise amplifies ambiguity, increasing complexity.  

---

## **6. Limitations**  
1. **Key Reuse**: Reusing \( K_{\text{msg}} \) leaks statistical patterns.  
2. **Padding Filtering**: Adversaries can identify noise if \( \mathcal{S} \) is known.  
3. **Computational Overhead**: Decryption requires \( O(128) \) hash computations per ciphertext element.  

---

## **7. Extensions**  
- **Hybrid Encryption**: Use \( K_{\text{msg}} \) to encrypt a symmetric key (e.g., AES-256).  
- **Authentication**: Append \( \text{MAC}(K_{\text{msg}}, C) \) to detect tampering.  
