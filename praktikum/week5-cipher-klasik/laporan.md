# Laporan Praktikum Kriptografi

Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)  
Nama: Asmoko Khusnul Tri Maulana  
 NIM: 230202738  
 Kelas: 5IKRB

---

## 1. Tujuan

1. Menerapkan algoritma **Caesar Cipher** untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma **Vigenère Cipher** dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori

Cipher klasik merupakan metode kriptografi yang digunakan sejak zaman kuno untuk menyembunyikan pesan dengan cara mengganti atau menukar posisi huruf. Terdapat dua kelompok utama dalam cipher klasik, yaitu cipher substitusi (penggantian karakter) dan cipher transposisi (pertukaran posisi karakter). Cipher klasik bekerja berdasarkan operasi aritmetika modular sederhana pada huruf-huruf alfabet.

Caesar Cipher adalah jenis cipher substitusi monoalfabetik di mana setiap huruf dalam plaintext digeser sejauh k posisi tertentu dalam alfabet. Sementara Vigenère Cipher merupakan cipher polialfabetik yang menggunakan kunci berupa kata untuk menentukan pergeseran tiap huruf, sehingga lebih sulit diserang dibanding Caesar Cipher.
Adapun Transposisi Cipher tidak mengganti huruf, melainkan hanya menukar urutan huruf berdasarkan pola tertentu (misalnya jumlah kolom tetap).

Namun, cipher klasik tergolong lemah dalam konteks keamanan modern karena pola enkripsi yang dapat dianalisis melalui analisis frekuensi huruf. Metode ini memungkinkan penyerang untuk menebak kunci dengan menganalisis seberapa sering huruf muncul dalam ciphertext.

---

## 3. Alat dan Bahan

(- Python 3.12.10

- Visual Studio Code / editor lain
- Git dan akun GitHub
- Library tambahan (misalnya pycryptodome, jika diperlukan) )

---

## 4. Langkah Percobaan

(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:

1. Membuat file `caesar.py, vigenere.py, dan transpose.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar.py, python vigenere.py, dan python transpose.py`.)

---

## 5. Source Code

A. caesar.py

```python
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

B. vigenere.py

```python
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

C. transpose.py

```python
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

## 6. Hasil dan Pembahasan

(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).

- Berikan tabel atau ringkasan hasil uji jika diperlukan.
- Jelaskan apakah hasil sesuai ekspektasi.
- Bahas error (jika ada) dan solusinya.

Hasil eksekusi program Caesar Cipher:

![Hasil caesar](screenshot/hasil%201.png)
![Hasil vigenere](screenshot/hasil%202.png)
![Hasil transpose](screenshot/hasil3.png)
)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1: Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
  Jawab: Kelemahan Caesar Cipher adalah ruang kuncinya sangat kecil (hanya 25 kemungkinan), sehingga mudah diserang dengan brute force. Sementara Vigenère Cipher, meskipun lebih kuat, tetap rentan terhadap Kasiski examination dan analisis frekuensi jika panjang kunci diketahui.
- Pertanyaan 2: Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
  Jawab: Karena distribusi huruf pada bahasa alami seperti Bahasa Inggris atau Indonesia tidak merata. Cipher klasik hanya mengganti simbol tanpa mengubah frekuensi kemunculan huruf, sehingga pola statistik masih bisa dikenali.
- Pertanyaan 3: Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.
  Jawab: Cipher substitusi mengganti huruf dengan huruf lain, sedangkan transposisi menukar posisi huruf. Cipher substitusi lebih mudah dianalisis dengan frekuensi huruf, sementara transposisi sulit dibaca tanpa mengetahui panjang kunci, tetapi masih rentan terhadap anagram analysis.

---

## 8. Kesimpulan

Praktikum ini menunjukkan bahwa cipher klasik seperti Caesar, Vigenère, dan Transposisi dapat mengenkripsi dan mendekripsi pesan dengan baik, namun tingkat keamanannya rendah untuk aplikasi modern. Cipher klasik lebih cocok sebagai media pembelajaran dasar konsep kriptografi, bukan untuk pengamanan data nyata.

---

## 9. Daftar Pustaka

- Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson.
- Katz, J., & Lindell, Y. (2021). Introduction to Modern Cryptography (3rd ed.). CRC Press.
- Schneier, B. (2015). Applied Cryptography: Protocols, Algorithms, and Source Code in C (20th Anniversary ed.). Wiley.
- Singh, S. (2000). The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography. Anchor Books.
- Paar, C., & Pelzl, J. (2010). Understanding Cryptography: A Textbook for Students and Practitioners. Springer.

---

## 10. Commit Log

commit 0dfc99ddc847a60a3bd05bab32e0f5cd8ba8c034
Author: Asmoko Khusnul Tri Maulana <maulana.asmoko@gmail.com>
Date: 2025-11-13
