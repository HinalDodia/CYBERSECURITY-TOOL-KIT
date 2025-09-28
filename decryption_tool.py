import tkinter as tk
from tkinter import messagebox

# Caesar Cipher
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

# Reverse Cipher
def reverse_cipher(text):
    return text[::-1]

# Vigenère Cipher
def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - 97
            result += chr((ord(char) - offset - key_shift) % 26 + offset)
            key_index += 1
        else:
            result += char
    return result

# ROT13 Cipher'
def rot13_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 13) % 26 + base)
        else:
            result += char
    return result



def decrypt_ui():
    def decrypt_text():
        msg = entry.get()
        shift = int(shift_entry.get())
        keyword = key_entry.get()
        method = method_var.get()

        if method == "Caesar":
            result = caesar_decrypt(msg, shift)
        elif method == "Reverse":
            result = reverse_cipher(msg)
        elif method == "Vigenère":
            result = vigenere_decrypt(msg, keyword)
        elif method == "ROT13":
            result = rot13_cipher(msg)
        else:
            result = "Invalid Method"

        messagebox.showinfo("Decrypted", f"Decrypted Text:\n\n{result}")

    win = tk.Toplevel()
    win.title("Decrypt Message")
    win.geometry("400x350")
    win.config(bg="#1e1e2f")

    tk.Label(win, text="Enter Encrypted Text:", bg="#1e1e2f", fg="white").pack(pady=5)
    entry = tk.Entry(win, width=40)
    entry.pack()

    tk.Label(win, text="Enter Caesar Shift (if selected):", bg="#1e1e2f", fg="white").pack(pady=5)
    shift_entry = tk.Entry(win, width=5)
    shift_entry.insert(0, "3")
    shift_entry.pack()

    tk.Label(win, text="Enter Vigenère Keyword:", bg="#1e1e2f", fg="white").pack(pady=5)
    key_entry = tk.Entry(win, width=20)
    key_entry.insert(0, "key")
    key_entry.pack()

    method_var = tk.StringVar(value="Caesar")
    methods = ["Caesar", "Reverse", "Vigenère", "ROT13"]
    for m in methods:
        tk.Radiobutton(win, text=f"{m} Cipher", variable=method_var, value=m, bg="#1e1e2f", fg="white").pack()

    tk.Button(win, text="Decrypt", command=decrypt_text).pack(pady=10)

    win.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Decryption Tool")
    root.geometry("300x200")
    root.config(bg="#1e1e2f")

    tk.Button(root, text="Open Decryption Tool", command=decrypt_ui).pack(pady=50)

    root.mainloop()

