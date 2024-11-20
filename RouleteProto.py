import tkinter as tk
from tkinter import messagebox
import random
import math
import time

def add_name():
    """Tambahkan nama ke list."""
    new_name = entry.get().strip()
    if new_name:
        names.append(new_name)
        listbox.insert(tk.END, new_name)
        entry.delete(0, tk.END)
        draw_wheel()
        draw_arrow()

def reset_names():
    """Reset daftar nama."""
    names.clear()
    listbox.delete(0, tk.END)
    result_label.config(text="")
    draw_wheel()
    draw_arrow()

def spin_wheel():
    """Putar roda dengan animasi."""
    global current_angle
    
    if not names:
        result_label.config(text="Tambahkan elemen terlebih dahulu!", fg="red")
        return

    result_label.config(text="Spinning...", fg="white")
    root.update()

    spins = random.randint(30, 50)
    speed = 0.01
    for _ in range(spins):
        current_angle = (current_angle + 15) % 360
        draw_wheel()
        draw_arrow()
        root.update()
        time.sleep(speed)
        speed += 0.005

    # Menghitung pemenang berdasarkan posisi panah
    sector_size = 360 / len(names)
    
    # Menyesuaikan sudut karena panah di sebelah kanan (0 derajat)
    # Dan roda berputar berlawanan arah jarum jam
    adjusted_angle = (360 - current_angle) % 360
    
    # Menghitung indeks yang sesuai dengan posisi panah
    index = int(adjusted_angle / sector_size)
    if index >= len(names):
        index = 0
        
    final_choice = names[index]
    
    messagebox.showinfo("Pemenang!", f"Selamat kepada:\n\n{final_choice}")
    result_label.config(text=f"Pemenang: {final_choice}", fg="green")

def draw_wheel():
    """Gambar roda dan bagiannya di Canvas."""
    canvas.delete("all")
    num_names = len(names)
    if num_names == 0:
        return

    center_x = 200  # Posisi x dari tengah roda
    center_y = 200  # Posisi y dari tengah roda
    radius = 150    # Radius roda

    if num_names == 1:
        print("Menggambar roda merah penuh")
        canvas.create_oval(50, 50, 350, 350, fill="red", outline="white", width=2)
        canvas.create_text(center_x, center_y, 
                           text=names[0], 
                           fill="white", 
                           font=("Arial", 16, "bold"))
        return
    print("Menggambar roda dengan banyak elemen")
    angle_per_sector = 360 / num_names
    start_angle = current_angle

    # Tambahkan lingkaran luar sebagai border
    canvas.create_oval(50, 50, 350, 350, outline="white", width=2)

    for i, name in enumerate(names):
        end_angle = start_angle + angle_per_sector

        # Gambar sektor
        canvas.create_arc(50, 50, 350, 350, 
                            start=start_angle, 
                            extent=angle_per_sector,
                            fill=colors[i % len(colors)], 
                            outline="white", 
                            tags="wheel")

        # Sesuaikan posisi dan rotasi teks
        text_angle = math.radians((start_angle + end_angle) / 2)
        x = center_x + (radius * 0.7) * math.cos(text_angle)
        y = center_y - (radius * 0.7) * math.sin(text_angle)

        # Rotasi teks agar lebih mudah dibaca
        rotation = (start_angle + angle_per_sector / 2) + 90
        if 90 <= rotation <= 270:
            rotation += 180

        canvas.create_text(x, y, 
                            text=name, 
                            fill="white", 
                            font=("Arial", 12, "bold"), 
                            angle=rotation,
                            tags="wheel")

        start_angle = end_angle

    """Gambar roda dan bagiannya di Canvas."""
    canvas.delete("all")
    num_names = len(names)
    if num_names == 0:
        return

    # Gambar roda
    angle_per_sector = 360 / num_names
    start_angle = current_angle
    center_x = 200
    center_y = 200
    radius = 150  # Radius roda

    # Tambahkan lingkaran luar sebagai border
    canvas.create_oval(50, 50, 350, 350, outline="white", width=2)

    for i, name in enumerate(names):
        end_angle = start_angle + angle_per_sector

        # Gambar sektor
        canvas.create_arc(50, 50, 350, 350, 
                         start=start_angle, 
                         extent=angle_per_sector,
                         fill=colors[i % len(colors)], 
                         outline="white", 
                         tags="wheel")

        # Sesuaikan posisi dan rotasi teks
        text_angle = math.radians((start_angle + end_angle) / 2)
        x = center_x + (radius * 0.7) * math.cos(text_angle)
        y = center_y - (radius * 0.7) * math.sin(text_angle)
        
        # Rotasi teks agar lebih mudah dibaca
        rotation = (start_angle + angle_per_sector / 2) + 90
        if 90 <= rotation <= 270:
            rotation += 180

        canvas.create_text(x, y, 
                         text=name, 
                         fill="white", 
                         font=("Arial", 12, "bold"), 
                         angle=rotation,
                         tags="wheel")

        start_angle = end_angle

def draw_arrow():
    # Gambar panah di sisi kanan yang mengarah ke dalam
    arrow_size = 20
    arrow_base = 15
    arrow_x = 350  # Posisi x di sisi kanan roda
    arrow_y = 200  # Tengah vertikal

    # Titik-titik untuk membentuk panah yang mengarah ke dalam
    points = [
        arrow_x, arrow_y,  # Ujung panah (paling kiri)
        arrow_x + arrow_base, arrow_y - arrow_size,  # Ujung atas
        arrow_x + arrow_base, arrow_y + arrow_size,  # Ujung bawah
    ]
    
    # Buat panah yang mengarah ke dalam dan tidak berputar
    canvas.create_polygon(
        points,
        fill="silver",
        outline="white",
        width=2,
        tags="indicator"
    )

    # Gambar panah di sisi kanan yang mengarah ke dalam
    arrow_size = 20
    arrow_base = 15
    arrow_x = 350  # Posisi x di sisi kanan roda
    arrow_y = 200  # Tengah vertikal

    # Titik-titik untuk membentuk panah yang mengarah ke dalam
    points = [
        arrow_x, arrow_y,  # Ujung panah (paling kiri)
        arrow_x + arrow_base, arrow_y - arrow_size,  # Ujung atas
        arrow_x + arrow_base, arrow_y + arrow_size,  # Ujung bawah
    ]
    
    # Buat panah yang mengarah ke dalam dan tidak berputar
    canvas.create_polygon(
        points,
        fill="silver",
        outline="white",
        width=2,
        tags="indicator"
    )
    
# Inisialisasi GUI
root = tk.Tk()
root.title("Wheel of Names")
root.geometry("500x700")
root.config(bg="#2b2b2b")

# Data
names = []
current_angle = 0
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Canvas untuk roda
canvas = tk.Canvas(root, width=400, height=400, bg="#2b2b2b", highlightthickness=0)
canvas.pack(pady=10)


# Frame untuk input dan tombol
frame = tk.Frame(root, bg="#2b2b2b")
frame.pack(pady=10)

# Konfigurasi kolom agar ukuran seragam
frame.columnconfigure(0, weight=1, uniform="group1")
frame.columnconfigure(1, weight=1, uniform="group1")
frame.columnconfigure(2, weight=1, uniform="group1")
frame.columnconfigure(3, weight=1, uniform="group1")

# Entry untuk input
entry = tk.Entry(frame, bg="white", justify="center", font=("Arial", 12))
entry.grid(row=0, column=0, sticky="nsew", padx=5, pady=5, ipady=5)

# Tombol Tambahkan
add_button = tk.Button(frame, text="Tambahkan", command=add_name, 
                      bg="green", fg="white", font=("Arial", 12), width=12, height=1)
add_button.grid(row=0, column=1, padx=5, pady=5)

# Tombol Reset
reset_button = tk.Button(frame, text="Reset", command=reset_names, 
                        bg="red", fg="white", font=("Arial", 12), width=12, height=1)
reset_button.grid(row=0, column=2, padx=5, pady=5)

# Tombol SPIN
spin_button = tk.Button(frame, text="SPIN!", command=spin_wheel, 
                       bg="#f39c12", fg="white", font=("Arial", 12, "bold"), 
                       width=12, height=1)
spin_button.grid(row=0, column=3, padx=5, pady=5)


# Listbox label
listbox_label = tk.Label(root, text="Daftar Nama:", bg="#2b2b2b", fg="white", font=("Arial", 12))
listbox_label.pack()

# Listbox
listbox = tk.Listbox(root, width=30, height=10, bg="#3b3b3b", fg="white", 
                     selectbackground="green", relief=tk.SOLID, bd=1)
listbox.pack(pady=10)

# Label hasil
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), 
                       bg="#2b2b2b", fg="white")
result_label.pack(pady=10)

# Gambar roda awal
draw_wheel()

root.mainloop()
