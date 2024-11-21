import tkinter as tk
from tkinter import messagebox
import random
import math
import time
import pygame   # Tambahkan ini untuk suara
import os  

# Inisialisasi Pygame untuk suara
pygame.mixer.init()

def tambah():
    """Tambahkan nama ke list."""
    new_name = entry.get().strip()
    if new_name:
        names.append(new_name)
        listbox.insert(tk.END, new_name)
        entry.delete(0, tk.END)
        draw_wheel()
        panah()

def hapus():
    """Hapus nama yang dipilih dari list dan perbarui roda."""
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        names.pop(index)
        listbox.delete(index)
        result_label.config(text="")
        draw_wheel()
        panah()

def resets():
    """Reset daftar nama."""
    names.clear()
    listbox.delete(0, tk.END)
    result_label.config(text="")
    draw_wheel()
    panah()

def play_sound():
    sound_file = os.path.join(os.path.dirname(__file__), "Pemenang.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def spin_wheel():
    """Putar roda dengan animasi selama sekitar 9 detik, terlepas dari jumlah elemen."""
    global current_angle

    total_duration = 9  # Total durasi putaran dalam detik
    spins = 100  # Jumlah langkah untuk mencapai total durasi
    speed = total_duration / (spins ** 1.5)  # Kecepatan awal animasi
    angle_per_step = 15  # Besar sudut per langkah, tetap terlepas dari jumlah elemen

    for i in range(spins):
        current_angle = (current_angle + angle_per_step) % 360  # Tambah sudut tetap setiap langkah
        draw_wheel()
        panah()
        root.update()
        
        time.sleep(speed)
        # Perlambatan progresif
        speed *= 1.02  # Secara bertahap menambah jeda setiap langkah

    # Menghitung pemenang berdasarkan posisi panah
    if len(names) > 0:
        sector_size = 360 / len(names)
        adjusted_angle = (360 - current_angle) % 360
        index = int(adjusted_angle / sector_size)
        if index >= len(names):
            index = 0

        final_choice = names.pop(index)  # Hapus pemenang dari daftar
        listbox.delete(index)  # Hapus pemenang dari Listbox
        
        # Mainkan suara saat pemenang muncul
        play_sound()
        messagebox.showinfo("You got a choice!", f"Pilihan untukmu adalah:\n\n{final_choice}")
        result_label.config(text=f"Pemenang: {final_choice}")

    draw_wheel()
    panah()

def draw_wheel():
    """Gambar roda dan bagiannya di Canvas."""
    canvas.delete("all")
    num_names = len(names)
    
    # Gunakan koordinat yang sama untuk lingkaran silver dan lingkaran data
    center_x = 200  # Posisi x dari tengah roda
    center_y = 200  # Posisi y dari tengah roda
    radius_outer = 150  # Radius lingkaran luar
    
    # Gambar lingkaran dasar dengan ukuran tetap (silver jika belum ada data)
    if num_names == 0:
        canvas.create_oval(
            center_x - radius_outer, center_y - radius_outer,
            center_x + radius_outer, center_y + radius_outer,
            fill="silver", outline="white"
        )
        return

    angle_per_sector = 360 / num_names
    start_angle = current_angle

    # Tambahkan lingkaran luar sebagai border
    canvas.create_oval(
        center_x - radius_outer, center_y - radius_outer,
        center_x + radius_outer, center_y + radius_outer,
        outline="white", width=2
    )

    if num_names == 1:
        canvas.create_oval(50, 50, 350, 350, fill="#F9B7FF", outline="white", width=2)
        canvas.create_text(center_x, center_y, 
                           text=names[0], 
                           fill="black", 
                           font=("Arial", 16, "bold"))
        return

    for i, name in enumerate(names):
        end_angle = start_angle + angle_per_sector

        # Gambar sektor
        canvas.create_arc(
            center_x - radius_outer, center_y - radius_outer,
            center_x + radius_outer, center_y + radius_outer,
            start=start_angle,
            extent=angle_per_sector,
            fill=colors[i % len(colors)],
            outline="white",
            tags="wheel"
        )

        # Posisi dan rotasi teks di setiap sektor
        text_angle = math.radians((start_angle + end_angle) / 2)
        text_radius = radius_outer * 0.7
        x = center_x + text_radius * math.cos(text_angle)
        y = center_y - text_radius * math.sin(text_angle)

        # Tentukan rotasi teks agar mudah dibaca
        rotation = (start_angle + angle_per_sector / 2) + 90
        if 90 <= rotation <= 270:
            rotation += 180

        canvas.create_text(
            x, y,
            text=name,
            fill="black",
            font=("Arial", 12, "bold"),
            angle=rotation,
            tags="wheel"
        )

        start_angle = end_angle

def panah():
    # Gambar panah di sisi kanan yang mengarah ke dalam
    arrow_size = 20
    arrow_base = 15
    arrow_x = 350  # Posisi x di sisi kanan roda
    arrow_y = 200  # Tengah vertikal

    points = [
        arrow_x, arrow_y,
        arrow_x + arrow_base, arrow_y - arrow_size,
        arrow_x + arrow_base, arrow_y + arrow_size,
    ]
    
    canvas.create_polygon(
        points,
        fill="#9F000F",
        outline="black",
        width=2,
        tags="indicator"
    )

# Inisialisasi GUI
root = tk.Tk()
root.title("Twist & Turn")
root.geometry("500x700")
root.config(bg="black")

names = []
current_angle = 0
colors = ["#F9B7FF", "#EDE6D6", "#E0B0FF", "#9E7BFF", "#822EFF", "#736AFF", "#D291BC", 
          "#D462FF", "#FF77FF", "#FF69B4", "#FFB2D0", "#F8B88B", "#F75D59", "#FF8674", 
          "#FFA07A", "#8A865D", "#E9AB17", "#BCB88A", "#FBB117", "#FFDAB9", 
          "#64E986", "#A0D6B4", "#A0D6B4"]

canvas = tk.Canvas(root, width=400, height=400, highlightthickness=0, bg="black")
canvas.pack(pady=10)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

frame.columnconfigure(0, weight=1, uniform="group1")
frame.columnconfigure(1, weight=1, uniform="group1")
frame.columnconfigure(2, weight=1, uniform="group1")
frame.columnconfigure(3, weight=1, uniform="group1")

entry = tk.Entry(frame, bg="white", justify="center", font=("Arial", 12))
entry.grid(row=0, column=0, sticky="nsew", padx=5, pady=5, ipady=5)

add_button = tk.Button(frame, text="Tambahkan", command=tambah, bg="green", fg="black", font=("Arial", 12), width=12, height=1)
add_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(frame, text="Hapus", command=hapus, bg="orange", fg="black", font=("Arial", 12), width=12, height=1)
delete_button.grid(row=0, column=2, padx=5, pady=5)

reset_button = tk.Button(frame, text="Reset", command=resets, bg="red", fg="black", font=("Arial", 12), width=12, height=1)
reset_button.grid(row=0, column=3, padx=5, pady=5)

spin_button = tk.Button(frame, text="SPIN!", command=spin_wheel, bg="#f39c12", fg="black", font=("Arial", 12, "bold"), width=12, height=1)
spin_button.grid(row=0, column=4, padx=5, pady=5)

listbox_label = tk.Label(root, text="Daftar Nama:", bg="black", fg="white", font=("Arial", 12))
listbox_label.pack()

listbox = tk.Listbox(root, width=30, height=10, bg="#DADBDD", fg="black", relief=tk.SOLID, bd=1)
listbox.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="black", fg="white")
result_label.pack(pady=10)

draw_wheel()

root.mainloop()
