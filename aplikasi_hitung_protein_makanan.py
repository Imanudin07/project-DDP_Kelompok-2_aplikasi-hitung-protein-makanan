import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class AplikasiHitungProtein:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Hitung Protein Makanan")

        # Variabel String Tkinter untuk input
        self.nama_var = tk.StringVar()
        self.protein_var = tk.StringVar()
        self.lemak_var = tk.StringVar()
        self.karbohidrat_var = tk.StringVar()

        # Membuat dan menata elemen GUI
        self.buat_ui()

    def hitung_protein(self):
        try:
            protein = float(self.protein_var.get())
            lemak = float(self.lemak_var.get())
            karbohidrat = float(self.karbohidrat_var.get())

            # Menghitung total protein
            total_protein = protein + (lemak + karbohidrat) * 0.25

            # Menampilkan hasil
            self.hasil_label.config(text=f"Total Protein: {total_protein:.2f} gram", font=("Arial", 14, "bold"))

        except ValueError:
            self.hasil_label.config(text="Masukkan angka valid untuk semua bidang", font=("Arial", 12))

    def buat_ui(self):
        style = Style(theme='vapor')  # Ganti dengan tema yang diinginkan

        frame = ttk.Frame(self.root, padding="20 20 20 20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Nama Makanan:").grid(row=0, column=0, sticky=tk.E)
        nama_entry = ttk.Entry(frame, textvariable=self.nama_var)
        nama_entry.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(frame, text="Protein (gram):").grid(row=1, column=0, sticky=tk.E)
        protein_entry = ttk.Entry(frame, textvariable=self.protein_var)
        protein_entry.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(frame, text="Lemak (gram):").grid(row=2, column=0, sticky=tk.E)
        lemak_entry = ttk.Entry(frame, textvariable=self.lemak_var)
        lemak_entry.grid(row=2, column=1, sticky=tk.W)

        ttk.Label(frame, text="Karbohidrat (gram):").grid(row=3, column=0, sticky=tk.E)
        karbohidrat_entry = ttk.Entry(frame, textvariable=self.karbohidrat_var)
        karbohidrat_entry.grid(row=3, column=1, sticky=tk.W)

        hitung_button = ttk.Button(frame, text="Hitung Protein", command=self.hitung_protein)
        hitung_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.hasil_label = ttk.Label(frame, text="Total Protein: ---", font=("Arial", 12))
        self.hasil_label.grid(row=5, column=0, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiHitungProtein(root)

    # Menentukan ukuran jendela
    root.geometry("500x400")

    root.mainloop()
